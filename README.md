# Archives Unleashed Cloud: Jupyter Notebooks
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/archivesunleashed/auk-notebooks/master?filepath=auk-notebook-example.ipynb)
[![Docker Stars](https://img.shields.io/docker/stars/archivesunleashed/auk-notebooks.svg)](https://hub.docker.com/r/archivesunleashed/auk-notebooks/)
[![Docker Pulls](https://img.shields.io/docker/pulls/archivesunleashed/auk-notebooks.svg)](https://hub.docker.com/r/archivesunleashed/auk-notebooks/)
[![LICENSE](https://img.shields.io/badge/license-Apache-blue.svg?style=flat-square)](./LICENSE)
[![Contribution Guidelines](http://img.shields.io/badge/CONTRIBUTING-Guidelines-blue.svg)](./CONTRIBUTING.md)

[Jupyter](https://jupyter.org/) notebooks to assist in creating additional analysis and visualizations of Archives Unleashed Cloud derivatives.

![notebook screenshot](https://user-images.githubusercontent.com/3834704/53252943-1a89b880-368e-11e9-9a9a-31c43a045a55.png)

## Requirements

We suggest using [Docker](https://www.docker.com/get-started), or [Anaconda Distribution](https://www.anaconda.com/distribution).

* [Python](https://www.python.org/downloads/) 3.7+
* [Jupyter Notebook](https://jupyter.org) (1.0.0)
* [Matplotlib](https://matplotlib.org) (3.0.2)
* [Numpy](https://pypi.org/project/numpy/#history) (1.15.1)
* [Pandas](https://pandas.pydata.org) (0.23.4)
* [Networks](https://networkx.github.io) (2.2)
* [NLTK](https://www.nltk.org/install.html) (3.4)


## Usage

Anaconda is a package manager that can help you find packages and dependencies, including some of the most popular ones used in data science research analysis. To run the Jupyter Notebook via Anaconda run through the following:


### Local (Anaconda)

```bash
git clone https://github.com/archivesunleashed/auk-notebooks.git
cd auk-notebooks
jupyter notebook
```

> Once inside the notebook, you may have to run an additional cell to configure the NLTK dependency. To do this you can: _insert > cell below_ underneathe the user confirguration script and run 

```bash
nltk.download()
```

A separte window will pop up to download NLTK packages. Highlight _all_ and then click download. This may take a few minutes. Once complete you can return to the notebook and select _cell > run all_.


### Docker

Docker is a container-based virtual machine system that bundles dependencies together, this means you can build the docker image and it will work out of the box. To run the Jupyter Notebook via Docker, there are two options, Docker Hub and Docker Locally.  


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

> Note: You must grant the within-container notebook user or group [(NB_UID or NB_GID)](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#docker-options) write access to the host directory (e.g., sudo chown 1000 /some/host/folder/for/work).

## Types of Visualizations

There are several types of visualizations that you can produce in the Jupyter Notebook. 

* Basic Domain Analysis
* Text Analysis
* Sentiment Analysis
* Network Analysis


## Additional Resources

This repository also uses the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html), which provide some helpful options for [customizing](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#docker-options) the container environment.


## License

This application is available as open source under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

## Acknowledgments

This work is primarily supported by the [Andrew W. Mellon Foundation](https://uwaterloo.ca/arts/news/multidisciplinary-project-will-help-historians-unlock). Any opinions, findings, and conclusions or recommendations expressed are those of the researchers and do not necessarily reflect the views of the sponsors.
