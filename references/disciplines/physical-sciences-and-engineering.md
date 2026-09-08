# Physical sciences and engineering

## Concrete regression lessons

The [SN2 live case](../../examples/cross-discipline/chemistry-sn2/README.md) caught a generated electron-pair arrow with two heads. Independently count atoms and formal charges, distinguish full electron-pair heads from single-electron fishhooks, anchor tails at a lone pair or bond, and verify destinations. Partial bonds and transition states must not imply unclaimed intermediates. This methyl example is achiral and provides no stereochemical validation; stereospecific requests need their own source and projection checks.

## Chemistry and biochemistry

Verify chemical identity, atom mapping where claimed, bond order, formal charge, protonation context and stereochemistry. Balance reaction stoichiometry and charge before styling. Distinguish reaction, equilibrium, resonance, electron-pair movement and physical transport arrows. Source catalytic intermediates and conditions; do not fill gaps in a mechanism with plausible-looking chemistry. Use structure-aware tools for exact chemical drawings, then retain editable labels and clean vector geometry.

## Materials and nanoscience

State composition, phase, architecture, preparation or operating condition and scale. Check interface ordering and whether depicted grains, pores or particles are measured, representative or purely conceptual. Validate crystal orientation, lattice vectors, defects and coordination against structural evidence if those details carry meaning. Avoid ornamental atomic lattices that imply an unsupported structure. Multiscale panels require explicit scale transitions and non-scale notes.

## Physics, optics and astronomy

Establish reference frame, coordinate axes, sign and polarisation conventions as applicable. Verify boundary conditions, conservation relations and optical path connectivity. Distinguish rays, wavefronts, fields and particle trajectories. Derive quantitative energy diagrams, spectra and trajectories from defined models/data; label conceptual diagrams accordingly. Astronomical illustrations need observer viewpoint and spatial/time context; visual size, brightness or colour must not silently imply measurement.

## Electrical and semiconductor devices

Retain the existing device checks in the general science guide: selected architecture, terminals, carrier selectivity, layer ordering, interfaces and optical access. Verify device bias and operating mode before transport arrows. Keep conventional current distinct from carrier motion. Source any energy offsets, thicknesses or performance values.

## Mechanical, civil and chemical engineering

Identify assembly relationships, mating surfaces, load/fluid/thermal paths and operational state. Exploded spacing is not an operating gap. Check inlet/outlet connections, valve states, system boundaries and mass/energy balances where relevant. Distinguish piping, wiring, signal lines and mechanical couplings with consistent symbols. Research current standards only when standards compliance is requested; do not imply certification from a conceptual illustration.

## Tool boundary

Use CAD or specialised solvers for tolerance-controlled manufacture, structural stress, electromagnetic fields, CFD or quantitatively correct geometry. Image2 can provide an editorial visual direction, but it is not a solver. Reconstruct scientifically meaningful SVG geometry, not a fake vector copy of a raster simulation.
