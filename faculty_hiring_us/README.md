# Faculty Hiring Networks (US)

Faculty hiring flows between 3,284 US universities across 107 academic fields. A directed edge from university *i* to university *j* means a faculty member received their PhD from *i* and was hired at *j*.

| Property | Value |
|----------|-------|
| Nodes | 3,284 universities |
| Edges | ~62,000 hiring events |
| Directed | Yes |
| Temporal | No |
| Node metadata | Domain |
| Edge metadata | Field (107 types) |
| Source | [Netzschleuder](https://networks.skewed.de/net/faculty_hiring_us) |

## Model variants

- **Edge groups**: Which academic fields drive university prestige rankings?
- **Node groups**: Rankings disaggregated by domain

## Data format

The download script fetches `academia.gt.zst`, the full cross-domain network. Domain- and field-specific subnetworks (e.g. `domain_engineering.gt.zst`, `field_computer_science.gt.zst`) are also available on Netzschleuder.

## Download

```bash
python download.py
```

## Citation

Wapman KH, Zhang S, Clauset A, Larremore DB (2022) Quantifying hierarchy and dynamics in US faculty hiring and retention. *Nature* 610: 120--127.
