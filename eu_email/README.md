# EU Email Communication Network

Email communication network from a large European research institution, spanning from October 2003 to May 2005. Each directed edge represents an email sent from one person to another, with a Unix timestamp.

| Property | Value |
|----------|-------|
| Nodes | 265,214 email addresses |
| Edges | ~420,000 emails |
| Directed | Yes |
| Temporal | Yes (2003--2005) |
| Source | [SNAP](https://snap.stanford.edu/data/email-EuAll.html) |

## Model variants

- **Scalability**: Largest network in this collection (265K nodes) -- tests first-order optimization at scale
- **Time-varying**: Email patterns over 20 months

## Data format

Downloaded as a text edge list: each line contains `source_id target_id`. A separate file maps node IDs to departments.

## Download

```bash
python download.py
```

## Citation

Leskovec J, Kleinberg J, Faloutsos C (2007) Graph evolution: Densification and shrinking diameters. *ACM TKDD* 1(1): 2.
