# Makefile to ease trivial tasks for the project

VENV="$(shell find . -name ".*env")"
IN_VENV="$(shell [ "/usr/local/bin/python" = $(shell which python) ] && \
	echo 0 || echo 1)"
REQ=requirements.txt


.PHONY: run
run:
	# run the Flask server
	@python local.py ${PORT}


.PHONY: clean
clean:
	# remove Python cache and temporary files
	@find . -name "*.pyc" -type f -delete
