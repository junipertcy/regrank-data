# Bitcoin OTC Trust Network

Trust ratings between members of the Bitcoin OTC trading platform. Users rate each other on a scale of -10 (total distrust) to +10 (total trust) to establish reputation for over-the-counter bitcoin trading.

| Property | Value |
|----------|-------|
| Nodes | 5,881 users |
| Edges | ~35,600 ratings |
| Directed | Yes |
| Temporal | Yes (timestamped) |
| Edge metadata | Signed weight (-10 to +10) |
| Source | [SNAP](https://snap.stanford.edu/data/soc-sign-bitcoin-otc.html) |

## Model variants

- **Robust (Huber)**: Extreme negative ratings as outliers -- ideal for demonstrating Huber loss
- **Time-varying**: Trust evolution as the platform grows

## Data format

Downloaded CSV with columns: `source`, `target`, `rating`, `time` (Unix timestamp).

## Download

```bash
python download.py
```

## Citation

Kumar S, Spezzano F, Suber VS, Faloutsos C (2016) Edge weight prediction in weighted signed networks. *IEEE ICDM*.
