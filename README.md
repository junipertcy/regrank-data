# regrank-data

Benchmark datasets for [regrank](https://github.com/junipertcy/regrank), a Python library for regularized SpringRank models on directed networks.

## Datasets

Sorted by network size (nodes). Each dataset demonstrates specific model variants of regularized SpringRank.

| Dataset | Domain | Nodes | Edges | Temporal | Source |
|---------|--------|------:|------:|:--------:|--------|
| [Dutch School](dutch_school/) | Education | 26 | ~200 | 4 snapshots | Netzschleuder |
| [Parakeet](parakeet/) | Animal behavior | 40 | ~960 | 4 quarters | Dryad |
| [PhD Exchange](PhD_exchange/) | Academia | 230 | ~9.5K | 1946--2010 | Taylor et al. |
| [Austrian Migrations](at_migrations/) | Demography | 2,115 | ~2.9M | 2002--2022 | Netzschleuder |
| [US Air Traffic](us_air_traffic/) | Transportation | 2,278 | ~6.4M | 1990--present | Netzschleuder |
| [Faculty Hiring (US)](faculty_hiring_us/) | Academia | 3,284 | ~62K | -- | Netzschleuder |
| [Bitcoin OTC](bitcoin_otc/) | Finance | 5,881 | ~35.6K | timestamped | SNAP |
| [Chess](chess/) | Sports | 7,301 | ~65K | timestamped | Netzschleuder |
| [Reddit Hyperlinks](reddit_hyperlinks/) | Online social | 55,863 | ~858K | 2014--2017 | SNAP |
| [EU Email](eu_email/) | Communication | 265,214 | ~420K | 2003--2005 | SNAP |

## Model variant coverage

Each model variant of regularized SpringRank is tested by at least two datasets.

| Model variant | Datasets |
|---------------|----------|
| Time-varying | Dutch School, Parakeet, PhD Exchange, Austrian Migrations, US Air Traffic, Bitcoin OTC, Chess, EU Email |
| Robust (Huber) | Dutch School, Parakeet, Bitcoin OTC, Chess |
| Node groups | Austrian Migrations, Faculty Hiring |
| Edge groups | Faculty Hiring, Reddit Hyperlinks |
| Scalability | Reddit Hyperlinks, EU Email |

## Quick start

Datasets ship as lightweight download scripts. To fetch a dataset:

```bash
cd bitcoin_otc/
python download.py
```

Data files are downloaded into a `data/` subdirectory (gitignored). The two smallest datasets (Parakeet, PhD Exchange) are committed directly.

To use with the `regrank` library:

```python
import regrank

# Load a built-in dataset
data = regrank.datasets.load("parakeet")
```

## License

See [LICENSE](LICENSE) for this repository's license. Individual datasets retain their original licenses; see each dataset's README for source and citation information.

