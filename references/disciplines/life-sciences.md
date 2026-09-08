# Life sciences: checks before drawing and after every export

## Concrete regression lessons

For ecosystem diagrams, declare a pool/transfer graph. The [carbon case](../../examples/cross-discipline/ecology-carbon/README.md) checks nine carbon transfers separately from solar energy, including plant, animal and microbial respiration. A food-chain-only arrow set is insufficient for a carbon-cycle claim. Label omitted reservoirs, timescales and budgets; unmeasured pool sizes, flux widths and organism detail must not look like data. This qualitative example does not validate quantitative ecology or taxonomy.

## Biological context

Record organism/species, cell or tissue type, physiological/experimental state and spatial/time scale. Separate a general conceptual pathway from a specific experiment. Resolve meaningful uncertainty from primary literature and authoritative structure or organism databases, not visual familiarity. Do not generalise one model organism, cell line or assay to all biology.

## Compartments and topology

- Name compartments and define the side of each membrane. Follow a molecule or membrane domain through every panel; orientation must remain consistent during budding, fusion and transport.
- Check whether cargo crosses a membrane or is enclosed by membrane remodelling. Draw a closed boundary after scission and preserve the correct lumen/cytosol relationship.
- Anchor protein domains and coats to the sourced membrane side. Do not put cytosolic adaptor proteins inside an extracellularly derived vesicle lumen for visual convenience.
- Distinguish lipid bilayer, protein coat, cell wall and extracellular matrix. Their shapes, connections and mechanisms are not interchangeable.
- Treat accessory-factor omission as a captioned simplification. Omission must not create a false causal claim that the illustrated factor alone performs the entire process.

## Molecular information and mechanism

- Verify gene/protein naming, species conventions, compartment localisation and sequence direction. Check DNA/RNA strand orientation and enzyme movement if shown. Do not generate exact sequences, residues or structures from appearance.
- Use verified coordinates for structure claims; otherwise label protein glyphs as schematic. Particle counts and icon sizes are not stoichiometry unless explicitly sourced.
- Define activation, inhibition, binding, catalysis, transport and transcription arrows separately. State direct versus indirect links and established versus proposed mechanisms.
- Check substrate/product identity and nucleotide/cofactor dependence. Do not exchange ATP/GTP labels as generic energy symbols or invent a fixed number of hydrolysis events.
- For assay figures, distinguish preparation, measurement and inference; include controls when needed for interpretation. Generated microscopy-like illustrations must not be presented as micrographs or evidence.

## Anatomy, neuroscience and physiology

Verify anatomical orientation, named structures, connections and subject context using appropriate references. State whether the view is a section, surface projection or schematic. Neural connectivity, synaptic sign and signal propagation need separate verification. Keep research illustrations distinct from patient-specific diagnosis or treatment guidance.

## Ecology, evolution and agricultural systems

Define arrow meaning in food webs and exchange networks; preserve it consistently. Source species/traits, geography, seasonal context and relevant scale. A cladogram, phylogram, resemblance chart and historical timeline encode different meanings. Derive branch lengths, abundances and distributions from actual data when quantitative meaning is intended.

## Biology acceptance questions

Can a reader follow each species without impossible compartment crossings? Are boundaries, protein orientation, biochemical direction and physiological context consistent across all panels? Do the caption and legend disclose simplifications and evidential uncertainty? Does the editable SVG retain these relationships when exported?

The bundled cell-trafficking example exercises membrane topology and coat removal. It does not validate all of the subjects in this guide.
