# Austrian Internal Migrations

Internal migration flows between 2,115 Austrian municipalities from 2002 to 2022. Each directed edge encodes the number of people migrating from one municipality to another in a given year, disaggregated by nationality and sex.

| Property | Value |
|----------|-------|
| Nodes | 2,115 municipalities |
| Edges | ~2.9M directed flows |
| Directed | Yes |
| Temporal | Yes (2002--2022) |
| Node metadata | Municipality name |
| Edge metadata | Nationality, sex |
| Source | [Netzschleuder](https://networks.skewed.de/net/at_migrations) |

## Model variants

- **Node groups**: Rankings disaggregated by nationality or sex
- **Time-varying**: Two decades of migration dynamics

## Data format

Downloaded as a graph-tool `.gt.zst` archive containing temporal, weighted, directed edges with metadata.

## Download

```bash
python download.py
```

## Citation

Accessed via Netzschleuder. Original data from Statistik Austria.
