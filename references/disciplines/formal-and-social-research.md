# Formal, computational and social research

## Concrete regression lessons

The [DAG case](../../examples/cross-discipline/research-causal-dags/README.md) tests directed edges and selected path blocking/opening. Conditioning is an operation, not a newly created causal arrow. A blocked backdoor or mediated path does not imply overall independence when a direct path remains. State the estimand and graph assumptions; do not generalise an adjustment rule to arbitrary graphs.

The [MLP case](../../examples/neural-network/README.md) checks layer counts, adjacent-layer connectivity and column-vector matrix dimensions. Softmax is coupled across logits; backpropagation calculates gradients while an optimiser updates parameters. Architecture illustrations cannot establish empirical performance.

## Mathematics, statistics and computing

Define symbols, domains, dimensions and assumptions before illustration. Use deterministic tools for exact geometry, equations, graph layout and quantitative plots. Verify tensor shapes, data/control flow, algorithm stages and input/output relationships. A drawn architecture is not evidence that an algorithm has been implemented or benchmarked.

For statistical figures, retain sample sizes, uncertainty definition, axes and data provenance. Do not invent distributions, significance, convergence curves or performance numbers. Image2 may design a conceptual overview or illustrative surrounding elements; it must not generate the scientific data layer.

## Psychology, economics and social sciences

Define constructs, population, setting, time period and study design. Source definitions and empirical relationships. Distinguish a measured association, theoretical pathway and identified causal effect. Directed edges require an explicit meaning; a beautiful causal-looking diagram cannot establish identification. Show randomisation, selection, exclusions or feedback only when supported by the actual design.

Avoid using illustrative people, demographics or geographic icons to imply unmeasured traits or representativeness. For qualitative research, preserve whether categories and relationships are participants' reports, analysts' interpretations or theoretical propositions.

## Editable output

Use live equations/text where the target editor supports them, otherwise retain a documented editable mathematical source alongside vector exports. Name nodes/edges by meaning and verify labels after export. Keep the default PNG/SVG pair; document any user-requested format exception. Exact symbolic or data-driven figures may justify a direct deterministic route with image generation marked not applicable.
