# Chess Games

Outcomes of chess games between 7,301 players. Each directed edge represents a game won by the source player against the target player, with timestamps.

| Property | Value |
|----------|-------|
| Nodes | 7,301 players |
| Edges | ~65,000 games |
| Directed | Yes |
| Temporal | Yes (timestamped) |
| Edge metadata | Game outcome |
| Source | [Netzschleuder](https://networks.skewed.de/net/chess) |

## Model variants

- **Time-varying**: Player skill evolution over time
- **Robust (Huber)**: Upset results (low-ranked beating high-ranked) as outliers

## Data format

Downloaded as a graph-tool `.gt.zst` archive with directed edges encoding game outcomes and timestamps.

## Download

```bash
python download.py
```

## Citation

Accessed via Netzschleuder.
