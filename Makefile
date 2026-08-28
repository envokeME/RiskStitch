.PHONY: render check test validate list

render:
	python3 tools/render_patterns.py

check:
	python3 tools/render_patterns.py --check

test:
	python3 -m unittest discover -s tests -v

validate: check test

list:
	python3 scripts/list-patterns.py
