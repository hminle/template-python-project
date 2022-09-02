# template-research-project

A Template Repo for My Research Projects

## Init repo

1. `conda env create -n <env name>`
2. Install pre-commit: `conda install -c conda-forge pre-commit`
3. Run `pre-commit install`
4. `git add .`
5. `git commit -m "init repo"`
6. `git push origin main`

## Hydra

1. Get original project dir with `hydra utils`

```python
from hydra import utils as hydra_utils

@hydra.main()
def my_app(cfg: DictConfig) -> None:
    print(hydra_utils.get_original_cwd())
```

2. Get current working dir - where log and intermediate results are saved

```python
import os

print(os.getcwd())
```
