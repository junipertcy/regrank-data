# Parakeet Dominance Interactions

Aggressive dominance interactions among monk parakeets (*Myiopsitta monachus*) in two captive study groups, observed over four 6-day quarters.

| Property | Value |
|----------|-------|
| Nodes | 40 (21 in G1, 19 in G2) |
| Edges | ~960 directed interactions |
| Directed | Yes |
| Temporal | Yes (4 quarters) |
| Node metadata | Group (G1/G2) |
| Source | [Dryad](https://datadryad.org/stash/dataset/doi:10.5061/dryad.p56q7) |

## Model variants

- **Time-varying**: Ranking dynamics across 4 quarterly snapshots
- **Robust (Huber)**: Outlier interactions in small groups

## Data format

`aggXquarter.txt` is a tab-separated file with columns:

| Column | Description |
|--------|-------------|
| `group` | Study group (`G1` or `G2`) |
| `quarters` | Study quarter (1--4) |
| `actor` | 3-letter ID of the aggressor |
| `target` | 3-letter ID of the recipient |
| `number.wins` | Number of aggressive wins |

## Citation

Hobson EA, DeDeo S (2015) Social feedback and the emergence of rank in animal society. *PLOS Computational Biology* 11(9): e1004411.
