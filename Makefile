PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
PYTHON_BIN := $(VENV)/bin/python

setup: venv
	$(PIP) install -r requirement.txt

venv:
	$(PYTHON) -m venv $(VENV)


lint:
	$(VENV)/bin/ruff check *.py

ex%:
	$(PYTHON_BIN) -m src.$@.main

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf .pytest_cache


.PHONY: setup venv lint ex% clean