# Ubuntu 18.04
# https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile
FROM jupyter/base-notebook

# Metadata
LABEL maintainer="Nick Ruest <ruestn@gmail.com>"
LABEL description="Docker image for Archives Unleashed Cloud: Jupyter Notebooks"
LABEL website="https://archivesunleashed.org/"

# Install auk-notebook dependencies.
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt
RUN python -m nltk.downloader punkt vader_lexicon stopwords

# Copy auk-notebook files over.
COPY data $HOME/data
COPY auk-notebook.ipynb $HOME

# Start Jupyter Notebook.
CMD ["start-notebook.sh"]
