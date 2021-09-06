# e2x-nbtools

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DigiKlausur_e2x-nbtools&metric=alert_status)](https://sonarcloud.io/dashboard?id=DigiKlausur_e2x-nbtools)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DigiKlausur_e2x-nbtools&metric=coverage)](https://sonarcloud.io/dashboard?id=DigiKlausur_e2x-nbtools)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Tools for customizing jupyter notebook

## 1. Multiple checkpoints for jupyter notebook

This allows you to create more than one checkpoint for your notebook.

### 1.1 Installation

```
git clone https://github.com/DigiKlausur/e2x-nbtools
cd e2x-nbtools
pip install .
```

### 1.2 Enabling multiple checkpoints

Put a file called ```jupyter_notebook_config.py``` in one of the [configuration directories](https://jupyter.readthedocs.io/en/latest/use/jupyter-directories.html). Put the following content in this file:

```
# jupyter_notebook_config.py

from e2x_nbtools.contents.filecheckpoints import E2XFileCheckpoints

# Get an empty config
c = get_config()

# Register the new checkpoints
c.ContentsManager.checkpoint_class = E2XFileCheckpoints
# Set the number of checkpoints to keep
c.ContentsManager.checkpoint_class.number_of_checkpoints = 5
```

### 1.3 Enabling the frontend nbextension

To make sure the checkpoints are correctly displayed and updated in the notebook view you need to enable the ```checkpoints``` nbextension.

This can be done by typing the following in a terminal:
```
jupyter nbextension install e2x_nbtools --py --sys-prefix
jupyter nbextension enable e2x_nbtools/main --py --sys-prefix
```
