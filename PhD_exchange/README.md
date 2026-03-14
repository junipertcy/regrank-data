# PhD Exchange Network

Exchange of mathematics PhD graduates between US universities. A directed, weighted, temporal network where an edge from university *i* to university *j* with weight *w* in year *t* means *w* math PhDs graduated from *i* and later advised a PhD student at *j* who graduated in year *t*.

| Property | Value |
|----------|-------|
| Nodes | 230 universities |
| Edges | ~9,500 directed exchanges |
| Directed | Yes |
| Temporal | Yes (1946--2010) |
| Source | [Taylor et al.](https://sites.google.com/site/danetaylorresearch/data) |

## Model variants

- **Time-varying (l1/l2)**: Long temporal span reveals smooth and abrupt ranking shifts across decades

## Files

| File | Description |
|------|-------------|
| `PhD_exchange.txt` | Temporal edge list: `(i, j, w, t)` |
| `school_names.txt` | University names keyed by node index |
| `PhD_exchange_network.mat` | MATLAB file containing both variables |

## Citation

Taylor D, Myers SA, Clauset A, Porter MA, Mucha PJ (2017) Eigenvector-based centrality measures for temporal networks. *Multiscale Modeling & Simulation* 15(1): 537--574.
