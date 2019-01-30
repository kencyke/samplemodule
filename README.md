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

Formatter:

* [google/yapf](https://github.com/google/yapf)
* [ambv/black](https://github.com/ambv/black)

Linter:

* [PyCQA/pylint](https://github.com/PyCQA/pylint)
* [python/mypy](https://github.com/python/mypy)

Document Generator:

* [sphinx-doc/sphinx](https://github.com/sphinx-doc/sphinx)
