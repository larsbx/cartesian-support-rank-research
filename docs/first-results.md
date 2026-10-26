# First certificate search

All edge partitions are enumerated for six specified connected graphs. Candidate
tuple maps are checked for vertex injectivity, single-coordinate edge changes,
and nonconstant use of every coordinate. Factors can be complete graphs on the
coordinate labels; embeddings are ordinary, not induced.

| Graph | Maximum support found |
| --- | ---: |
| K2 | 1 |
| P3 | 2 |
| K3 | 1 |
| K2 square K2 | 2 |
| K2 square P3 | 3 |
| K2 square K3 | 2 |

The receipt includes edges, colors, actual tuple maps, and partition totals.
Collapsed maps are rejected as a negative control. The product examples agree
with additivity of the observed maxima, but the general additivity claim is an
open project question, not a search assumption. Exactness as r* requires the
completeness reduction in `proof/certificate-obligation.md` to be accepted.
