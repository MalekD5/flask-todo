dev:
	@livetw dev

build:
	@livetw build

test:
	@pytest -s $(filter-out $@,$(MAKECMDGOALS))

.PHONY: dev build test
