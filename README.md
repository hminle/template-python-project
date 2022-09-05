# template-research-project

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Last commit](https://img.shields.io/github/last-commit/hminle/template-research-project)](https://github.com/hminle/)
[![Top language](https://img.shields.io/github/languages/top/hminle/template-research-project)](https://github.com/hminle/)
[![Repo size](https://img.shields.io/github/repo-size/hminle/template-research-project)](https://github.com/hminle/)


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

## Acknowledgement

This template was heavily inspired by: [lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template). A big thank to [Łukasz Zalewski](https://github.com/ashleve) and contributors. I adopted many functions from that repo.

## License

This template is licensed under the MIT License.

```
MIT License

Copyright (c) 2021 ashleve

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
