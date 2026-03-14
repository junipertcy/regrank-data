# Reddit Hyperlink Network

Directed hyperlinks between subreddits on Reddit from 2014 to 2017. Each edge represents a post in the source subreddit that links to the target subreddit, annotated with sentiment (positive or negative).

| Property | Value |
|----------|-------|
| Nodes | 55,863 subreddits |
| Edges | ~858,000 hyperlinks |
| Directed | Yes |
| Temporal | Yes (2014--2017) |
| Node metadata | Subreddit category |
| Edge metadata | Signed sentiment |
| Source | [SNAP](https://snap.stanford.edu/data/soc-RedditHyperlinks.html) |

## Model variants

- **Scalability**: Large network with ~56K nodes
- **Edge groups**: Positive vs. negative sentiment links yield different rankings

## Data format

Downloaded TSV with columns including: `SOURCE_SUBREDDIT`, `TARGET_SUBREDDIT`, `POST_ID`, `TIMESTAMP`, `LINK_SENTIMENT`, `PROPERTIES`.

## Download

```bash
python download.py
```

## Citation

Kumar S, Hamilton WL, Leskovec J, Jurafsky D (2018) Community interaction and conflict on the web. *WWW 2018*.
