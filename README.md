# Thesaurus

To help your mind find words

This repo contains a truncated set of word vectors. It is highly recommended to download the full set here:

[GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)

## Setup

1. Create python virtual env with `python3 -m venv env`. This will create a directory `env` that will contain the python environment.
1. Activate virtual env: `source env/bin/activate`.
1. Install requirements: `pip install -r requirements.txt`
1. Start the server: `python app.py`
1. Access site at `http://localhost:6543`

## Deployment

You will need authorization for the project on google cloud. You will also need to have `kubectl` and `gcloud` cli tools installed.

You will also need to download the glove vectors (linked to above) and have the `glove.6B/glove.6B.300d.txt` file available at that exact path. This is configured as an environment variable in `deploy.yml` file under the deployment spec `spec.template.containers.env`

1. Authenticate with google cloud
```
make credentials
```

2. Build the container and push it
```
make build && make push
```

3. Rollout
```
make rollout
```
