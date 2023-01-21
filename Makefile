dev:
	fd .py | entr -cdr python main.py
.PHONY: dev

init:
	poetry install
.PHONY: init

browse:
	feh -. output
.PHONY: browse
