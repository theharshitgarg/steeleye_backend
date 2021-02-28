.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete


test:
	python -m pytest \
		-v \
		--cov=addition \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t addition:latest .

log: clean
	touch logfile.log

run: log
	python src/app/main.py