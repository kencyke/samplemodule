# Sample Python Module

This simple module is an example repository for Python 3.6+ projects.

Requirements:

* [pypa/pipenv](https://github.com/pypa/pipenv)
* [make](https://www.gnu.org/software/make/manual/)

To generate `requirements.txt` from `Pipfile`, run the following command:
```bash
pipenv lock -r | awk '{if(NR>1)print}' > requirements.txt
```

## Other Development Tools

The libraries listed below are not used in this module but recommended for sophistication.

Formatter/Linter/Type Checker:

* [google/yapf](https://github.com/google/yapf)
* [ambv/black](https://github.com/ambv/black)
* [PyCQA/pylint](https://github.com/PyCQA/pylint)
* [python/mypy](https://github.com/python/mypy)
* [Microsoft/pyright](https://github.com/Microsoft/pyright)
* [google/pytype](https://github.com/google/pytype)
* [facebook/pyre-check](https://github.com/facebook/pyre-check)

Test Runner:

* [facebookincubator/ptr](https://github.com/facebookincubator/ptr)

Document Generator:

* [sphinx-doc/sphinx](https://github.com/sphinx-doc/sphinx)
