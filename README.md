# Archives Unleashed Cloud: Jupyter Notebooks
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/archivesunleashed/auk-notebooks/master?filepath=auk-notebook-example.ipynb)
[![Docker Stars](https://img.shields.io/docker/stars/archivesunleashed/auk-notebooks.svg)](https://hub.docker.com/r/archivesunleashed/auk-notebooks/)
[![Docker Pulls](https://img.shields.io/docker/pulls/archivesunleashed/auk-notebooks.svg)](https://hub.docker.com/r/archivesunleashed/auk-notebooks/)
[![LICENSE](https://img.shields.io/badge/license-Apache-blue.svg?style=flat-square)](./LICENSE)
[![Contribution Guidelines](http://img.shields.io/badge/CONTRIBUTING-Guidelines-blue.svg)](./CONTRIBUTING.md)

[Jupyter](https://jupyter.org/) notebooks to assist in creating additional analysis and visualizations of Archives Unleashed Cloud derivatives.

![notebook screenshot](https://user-images.githubusercontent.com/3834704/53252943-1a89b880-368e-11e9-9a9a-31c43a045a55.png)

## Requirements

[Anaconda Distribution](https://www.anaconda.com/distribution/#download-section) is very helpful here.

* Python 3.7+
* [Jupyter Notebook](https://jupyter.org) (1.0.0)
* matplotlib (3.0.2)
* numpy (1.15.1)
* pandas (0.23.4)
* networkx (2.2)
* nltk (3.4)

## Usage

We suggest using [Docker](https://www.docker.com/get-started), or [Anaconda Distribution](https://www.anaconda.com/distribution).

### Docker Hub

```bash
docker run --rm -it -p 8888:8888 archivesunleashed/auk-notebooks
```

### Docker Locally

```bash
git clone https://github.com/archivesunleashed/auk-notebooks.git
cd auk-notebooks
docker build -t auk-notebook .
docker run --rm -it -p 8888:8888 auk-notebook
```

This repository comes with sample data, you can swap out the sample data with your own Archives Unleashed Cloud data.

```bash
docker run --rm -it -p 8888:8888 -v "/path/to/own/data:/home/jovyan/data" auk-notebook
```

> [You must grant the within-container notebook user or group (NB_UID or NB_GID) write access to the host directory (e.g., sudo chown 1000 /some/host/folder/for/work).](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#docker-options)

This repository also uses the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html), which provide [a lot of helpful options to take advantage of](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#docker-options).

### Local (Anaconda)

```bash
git clone https://github.com/archivesunleashed/auk-notebooks.git
cd auk-notebooks
jupyter notebook
```

## License

This application is available as open source under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

## Resources

The example dataset in the `data` directory was created with the [Archives Unleashed Cloud](https://cloud.archivesunleashed.org/), and is drawn from the [B.C. Teachers' Labour Dispute (2014)](https://archive-it.org/collections/4867), collected by the University of Victoria Libraries. We are grateful that they've allowed us to use this material. The full-text derivative file is a random sample (37,000 lines) of the complete file because of GitHub file size limitations.

If you use this material, please cite it along the following lines:

- Archives Unleashed Project. (2018). Archives Unleashed Toolkit (Version 0.17.0). Apache License, Version 2.0.
- University of Victoria Libraries, B.C. Teachers' Labour Dispute (2014), Archive-It Collection 4867, https://archive-it.org/collections/4867.

## Acknowledgments

This work is primarily supported by the [Andrew W. Mellon Foundation](https://uwaterloo.ca/arts/news/multidisciplinary-project-will-help-historians-unlock). Any opinions, findings, and conclusions or recommendations expressed are those of the researchers and do not necessarily reflect the views of the sponsors.
