#!/usr/bin/env python3
"""Validate a figure's recorded release evidence, not its scientific truth."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath
from audit_svg import audit

GATES = ("science", "visual", "typography", "editability", "portability", "provenance")


def check(record, base):
    errors = []
    if not isinstance(record, dict):
        return ["Review must be a JSON object"]
    base = Path(base).resolve()
    if record.get("schema_version") != 1:
        errors.append("Unsupported schema_version")
    if not isinstance(record.get("title"), str) or not record["title"].strip():
        errors.append("A figure title is required")
    delivery = record.get("delivery")
    if delivery not in {"raster", "full-vector", "hybrid"}:
        errors.append("delivery must be raster, full-vector or hybrid")
    registered = {}
    roles = set()
    files = record.get("files")
    if not isinstance(files, list):
        errors.append("files must be a list")
        files = []
    for item in files:
        if not isinstance(item, dict):
            errors.append("Each file entry must be an object")
            continue
        rel, role, sha = item.get("path"), item.get("role"), item.get("sha256")
        if not isinstance(rel, str) or not rel or "\\" in rel or PureWindowsPath(rel).drive or PurePosixPath(rel).is_absolute() or ".." in PurePosixPath(rel).parts:
            errors.append("File paths must be portable relative paths without traversal")
            continue
        if rel in registered:
            errors.append("Duplicate file path: " + rel)
            continue
        target = (base / rel).resolve()
        if not target.is_relative_to(base):
            errors.append("File resolves outside the project: " + rel)
            continue
        registered[rel] = target
        if not isinstance(role, str) or not role:
            errors.append("Missing file role: " + rel)
        else:
            roles.add(role)
        if not target.is_file():
            errors.append("Missing file: " + rel)
        elif not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{64}", sha) or hashlib.sha256(target.read_bytes()).hexdigest() != sha:
            errors.append("Missing or mismatched SHA-256: " + rel)

    def evidence(items, label):
        if not isinstance(items, list) or not items:
            errors.append(label + " needs registered evidence files")
        else:
            for rel in items:
                if not isinstance(rel, str) or rel not in registered:
                    errors.append(label + " refers to unregistered evidence")

    gen = record.get("generation", {})
    if not isinstance(gen, dict):
        errors.append("generation must be an object")
        gen = {}
    for flag in ("exact_model_required", "claims_highest_verified"):
        if not isinstance(gen.get(flag), bool):
            errors.append(flag + " must be a boolean")
    if not isinstance(gen.get("controls_sent"), dict):
        errors.append("controls_sent must record an object of actual tool parameters")
    required_roles = {"brief", "sources", "preview", "caption", "visual-comparison"}
    if gen.get("status") == "not_applicable":
        if not isinstance(gen.get("reason"), str) or not gen["reason"].strip():
            errors.append("Generation exemption requires a reason")
        if gen.get("exact_model_required") or gen.get("claims_highest_verified"):
            errors.append("An unexecuted generation cannot satisfy model claims")
    elif gen.get("status") == "complete":
        required_roles |= {"prompt", "master"}
        if gen.get("route") not in {"codex-native", "authorised-api"} or not gen.get("tool"):
            errors.append("Completed generation requires its actual route and tool")
        if gen.get("reported_model"):
            evidence(gen.get("reported_model_evidence"), "Reported model")
        if gen.get("exact_model_required") and not gen.get("reported_model"):
            errors.append("Exact model requirement is unresolved")
        elif gen.get("exact_model_required") and gen.get("reported_model") != gen.get("requested_model"):
            errors.append("Exact model requirement does not match the reported model")
        if gen.get("claims_highest_verified"):
            if not gen.get("reported_model"):
                errors.append("Highest-version claim requires reported model evidence")
            evidence(gen.get("highest_verification_evidence"), "Highest-version verification")
    else:
        errors.append("Generation is pending or failed")
    if delivery in {"full-vector", "hybrid"}:
        required_roles |= {"source", "edit-test"}
    for role in sorted(required_roles - roles):
        errors.append("Missing file role: " + role)
    gates = record.get("gates", {})
    if not isinstance(gates, dict):
        errors.append("gates must be an object")
        gates = {}
    for name in GATES:
        gate = gates.get(name, {})
        if not isinstance(gate, dict):
            errors.append(name + " gate must be an object")
            continue
        status = gate.get("status")
        if status == "not_applicable" and name == "editability" and delivery == "raster":
            if not gate.get("notes"):
                errors.append("Editability exemption requires a reason")
            continue
        if status != "pass":
            errors.append(name + " gate has not passed")
        if not all(isinstance(gate.get(k), str) and gate[k].strip() for k in ("reviewer", "notes")):
            errors.append(name + " requires an identified reviewer and actual review notes")
        evidence(gate.get("evidence"), name)
    if not isinstance(record.get("unresolved"), list) or record["unresolved"]:
        errors.append("Unresolved defects must be an empty list for final release")
    if delivery == "full-vector":
        sources = [registered.get(i.get("path")) for i in files if isinstance(i, dict) and i.get("role") == "source"]
        svgs = [s for s in sources if s and s.suffix.lower() == ".svg" and s.is_file()]
        if not svgs:
            errors.append("This full-vector checker requires an SVG source")
        for source in svgs:
            try:
                errors.extend(source.name + ": " + err for err in audit(source, True, True)["errors"])
            except Exception as exc:
                errors.append("SVG inspection failed: " + str(exc))
    return errors


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("review", type=Path)
    args = p.parse_args()
    try:
        errors = check(json.loads(args.review.read_text(encoding="utf-8-sig")), args.review.parent)
    except (OSError, ValueError, TypeError) as exc:
        errors = [str(exc)]
    print(json.dumps({"evidence_checks_passed": not errors, "errors": errors,
                      "scope": "Bookkeeping and selected SVG checks only; not independent scientific or aesthetic certification."}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
