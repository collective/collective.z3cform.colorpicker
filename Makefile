all: run

run:
	docker-compose run --rm --service-ports  plone

makepattern:
	docker-compose run --rm --service-ports  plone makepattern

servepattern:
	docker-compose run --rm --service-ports  plone servepattern

shell:
	docker-compose run --rm --service-ports  plone /bin/bash

.PHONY: run makepattern servepattern
