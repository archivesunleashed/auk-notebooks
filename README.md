# Archives Unleashed Cloud: Jupyter Notebooks

[Jupyter](https://jupyter.org/) notebooks to assist in creating additional analysis and visualizations of Archives Unleashed Cloud derivatives.

![notebook screenshot](https://user-images.githubusercontent.com/3834704/53252943-1a89b880-368e-11e9-9a9a-31c43a045a55.png)

## Requirements

Jupyter Notebook. Follow the installation instructions on [their website](https://jupyter.org). 

Dependencies. Any version higher than below _should_ work:

* Python 3.7
* ggplot (0.11.5)
* matplotlib (3.0.2)
* numpy (1.15.1)
* pandas (0.23.4)
* networkx (2.2)
* nltk (3.4)

## Usage

We suggest using [Docker](https://www.docker.com/get-started):

```bash
git clone https://github.com/archivesunleashed/auk-notebooks.git
cd auk-notebooks
docker build -t auk-notebook .
docker run --rm -it -p 8888:8888 auk-notebook
```

If you have the dependencies installed:

```bash
git clone https://github.com/archivesunleashed/auk-notebooks.git
cd auk-notebooks
jupyter notebook
```

This repository comes with sample data, you can swap out the sample data with your own Cloud data.

```bash
docker run --rm -it -p 8888:8888 -v "/path/to/own/data:/home/jovyan/data" auk-notebook
```

## Contributing

Please see [contributing guidelines](https://github.com/archivesunleashed/auk-notebooks/blob/master/CONTRIBUTING.md) for details.

## License

This application is available as open source under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

## Acknowledgments

This work is primarily supported by the [Andrew W. Mellon Foundation](https://uwaterloo.ca/arts/news/multidisciplinary-project-will-help-historians-unlock). Any opinions, findings, and conclusions or recommendations expressed are those of the researchers and do not necessarily reflect the views of the sponsors.
