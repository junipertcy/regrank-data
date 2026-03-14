# Dutch School Friendships

Friendship nominations among 26 pupils in a Dutch school class, surveyed at 4 time points during 2003--2004. Each directed edge represents a friendship nomination from one pupil to another.

| Property | Value |
|----------|-------|
| Nodes | 26 |
| Edges | ~200 directed nominations |
| Directed | Yes |
| Temporal | Yes (4 snapshots) |
| Node metadata | Sex, age, ethnicity |
| Source | [Netzschleuder](https://networks.skewed.de/net/dutch_school) |

## Model variants

- **Robust (Huber)**: Small network where outlier nominations visibly affect rankings
- **Time-varying**: Friendship dynamics across 4 survey waves

## Data format

Downloaded as 4 graph-tool `.gt.zst` files (`klas12b-net-1` through `klas12b-net-4`), one per survey wave. Each graph has node properties `sex`, `age`, `ethnicity` and directed edges for friendship nominations.

## Download

```bash
python download.py
```

## Citation

Snijders TAB, van de Bunt GG, Steglich CEG (2010) Introduction to stochastic actor-based models for network dynamics. *Social Networks* 32(1): 44--60.
