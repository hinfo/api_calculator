tests:
	@python3 -m pytest -v --cov=app --cov=tests --cov-report xml
	@make pep8

pep8:
	@flake8 app --max-complexity=10 --ignore=S311,W503,W504
	@flake8 tests --ignore=S101,S311,W503,W504
	@echo tudo ok!