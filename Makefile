# Default values for user options
.PHONY: default
default: all

venv:
	rm -rf bin/ venv/
	#virtualenv -p python3.8 ./venv
	python3.8 -m venv ./venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
	venv/bin/pip install --upgrade wheel

	touch venv

bin/pip: setup.py requirements.txt
	venv/bin/pip install -r ./requirements.txt

	mkdir -p bin

	ln -sf $(PWD)/venv/bin/pip ./bin/pip
	ln -sf $(PWD)/venv/bin/main ./bin/main

	mkdir -p log
	mkdir -p var

all: venv bin/pip


.PHONY: clean
clean:
	rm -rf bin/ venv/

.PHONY: real-clean
real-clean:
	git clean -dfx
	rm -rf bin/ venv/

.PHONY: tags
tags:
	./venv-ctags venv/bin/python