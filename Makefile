##
# Snake
#
# @file
# @version 0.1
.PHONY:	run
run:
	python -m snake
test:
	python -m unittest discover
build:
	python setup.py sdist bdist_wheel
install:
	pip install dist/*.whl


# end
