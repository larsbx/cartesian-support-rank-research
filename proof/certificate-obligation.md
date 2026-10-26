# Certificate convention and completeness obligation

A certificate assigns a tuple to each pattern vertex. All tuples must differ;
each pattern edge changes precisely its declared coordinate; every coordinate
is nonconstant. Complete simple graphs on the used coordinate labels supply
valid factors. Nonedges need not be preserved.

The checker verifies these conditions without trusting the search's component
construction. A deliberately collapsed vertex map is rejected in every case.

The search enumerates every unlabeled partition of pattern edges into coordinates.
For each coordinate a it removes a-colored edges, takes the connected components
of the remaining graph, and uses those components as coordinate labels. It applies
no additivity upper-bound filter. It records valid witnesses, not a formal proof
of an exhaustive search theorem.

Completeness proof obligation: for any actual embedding with edge colors, show
each coordinate is constant on every such component. Thus these component labels
refine every realizable coordinate labeling; prove the refinement preserves each
edge's single-coordinate change and injectivity. Only after independent review
may maxima over partitions be promoted to exact r* values by this reduction.
The bound r*(G square H)<=r*(G)+r*(H) remains separate and unassumed.
