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

1. Do modular code.
1. Use classes with [_high cohesion_](https://stackoverflow.com/questions/10830135/what-is-high-cohesion-and-how-to-use-it-make-it).
1. Do unit tests when possible.

