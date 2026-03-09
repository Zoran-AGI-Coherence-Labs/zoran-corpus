.PHONY: reproduce_all test

reproduce_all:
	python3 src/demo_runner.py --all

test:
	python3 -m unittest discover -s src/tests -p 'test_*.py'
