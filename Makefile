init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	pipenv run detox

format:
	pipenv run sort
	pipenv run fix

clean:
	rm -rf .eggs .tox .pytest_cache build dist sample.egg-info

build:
	python setup.py sdist bdist bdist_wheel
	rm -rf build sample.egg-info

ci:
	pipenv run py.test --junitxml=report.xml

coverage:
	pipenv run py.test --verbose --cov-report term --cov-report xml --cov=sample tests
