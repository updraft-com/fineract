# API Tests

This uses the python py.test framework to setup and simulate a series of API tests
That run against a locally running (docker container) version of fineract

The goal is to simulate real-world API usage and simulate different patterns of usage
To ensure the fully integrated system behaves as expected

# How to run locally

1. Build fineract
2. Install the python environment -> you'll need poetry follow instructions here https://python-poetry.org/docs/

Initialise the python environment, run local docker image, and then run the tests

```
cd api-tests
poetry shell
poetry install
./manage.py start
py.test
```

