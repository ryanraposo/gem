# gem

gem is a turn-based strategy game where only the protagonist is aware of conflict. Traditional enemies are allies when your goal is unclear and your friends are always there to help... with something else.

With a procedurally-generated world and the option to add your friends’ characters to your own, there’s no limit to the possibilities.

Will you achieve?

## Development

Manual setup:

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html), an environment manager for Python
2. Create an env: `conda create -n gem python=3.9`
3. Activate that env: `conda activate gem`
4. Install pygame as you would normally with Python's premiere package manager, PIP: `pip install pygame`
5. To run, make sure the `gem` env is activated (`conda activate gem`), then: `py main.py`

To setup your env automatically, or troubleshoot a corrupted env:

1. Activate the `base` conda env: `conda activate base` or `conda deactivate`
2. Delete the `gem` env (if it exists): `conda env remove -n gem`
2. Setup env from file: `conda env create -f environment.yml`
