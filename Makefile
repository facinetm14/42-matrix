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

ex00:
	$(PYTHON_BIN) -m src.ex00.main

ex01:
	$(PYTHON_BIN) -m src.ex01.main

ex02:
	$(PYTHON_BIN) -m src.ex02.main

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf .pytest_cache


.PHONY: setup venv lint ex00 clean