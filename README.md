# Utils

This is a set of utilities that deliver a common functionality that I recurrently use
across several projects.

## How to install

```
pip install --upgrade git+https://github.com/rebordao/utils_py@master
```

## Architecture

```
.
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
├── setup.py
├── tests
│   └── __init__.py
└── utils_py
    ├── azure.py
    ├── __init__.py
    ├── slack_notifier.py
    └── utils.py
```

## Development Guidelines

1. Favour modular code.
1. Classes with [_high cohesion_](https://stackoverflow.com/questions/10830135/what-is-high-cohesion-and-how-to-use-it-make-it).
1. When possible classes and methods should have unit tests.

#### Test Coverage

You can run the following command (from root folder) to get the test 
coverage report written to the `htmlcov` folder:

```
PYTHONPATH=. py.test --cov-report html --cov=utils_py tests/ --verbose
```