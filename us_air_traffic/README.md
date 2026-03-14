# US Air Traffic

Passenger flows between US airports from 1990 to the present. Each directed edge represents the number of passengers flying from one airport to another in a given year, with carrier and service class metadata.

| Property | Value |
|----------|-------|
| Nodes | 2,278 airports |
| Edges | ~6.4M directed flows |
| Directed | Yes |
| Temporal | Yes (1990--present) |
| Node metadata | State, region |
| Edge metadata | Carrier, service class |
| Source | [Netzschleuder](https://networks.skewed.de/net/us_air_traffic) |

## Model variants

- **Time-varying (COVID changepoint)**: 30+ years of data spanning the COVID-19 disruption -- ideal for detecting abrupt ranking shifts
- **Edge groups**: Rankings by carrier or service class

## Data format

Downloaded as a graph-tool `.gt.zst` archive containing temporal, weighted, directed edges with node and edge metadata.

## Download

```bash
python download.py
```

## Citation

Accessed via Netzschleuder. Original data from the US Bureau of Transportation Statistics (T-100 Domestic Segment data).
