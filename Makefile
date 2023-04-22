.DEFAULT_GOAL = help

install: env  ## Install dependencies with poetry
	poetry install

serve-dev:  ## Run dev server
	poetry run python3 manage.py runserver 0.0.0.0:8081

serve-prod:  ## Run production server
	poetry run gunicorn --bind 0.0.0.0:8000 empty_blog.wsgi:application

migrate:  ## Apply migrations
	poetry run python3 manage.py migrate

migrations:  ## Make migrations
	poetry run python3 manage.py makemigrations

lint: ## Check lint
	poetry run flake8 .

test:  ## Run tests
	poetry run python3 manage.py test

check: lint test  ## Run lint and tests

help:  ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | sort \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[0;32m%-30s\033[0m %s\n", $$1, $$2}'

env:  ## Create or copy example as .env
	test ! -f .env && cp .env.example .env
