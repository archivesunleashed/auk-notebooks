# Ubuntu 18.04
# https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile
FROM jupyter/base-notebook

# Metadata
LABEL maintainer="Nick Ruest <ruestn@gmail.com>"
LABEL description="Docker image for the Archives Unleashed Notebooks"
LABEL website="https://archivesunleashed.org/"

RUN pip install ggplot==0.11.5 \
                matplotlib==3.0.2 \
                numpy==1.15.1 \
                pandas==0.23.4 \
                networkx==2.2 \
                nltk==3.4

# Hack to get around import error with pandas.
RUN sed -i 's/pandas.lib/pandas/g' /opt/conda/lib/python3.7/site-packages/ggplot/stats/smoothers.py

# Make things cleaner in Notebook
RUN rm -rf $HOME/work

# Copy auk-notebook files over.
COPY data $HOME/data
COPY nltk_data $HOME/nltk_data
COPY auk-notebook.ipynb $HOME
COPY auk-notebook-example.ipynb $HOME

# Start Jupyter Notebook
CMD ["start.sh", "jupyter", "notebook"]
