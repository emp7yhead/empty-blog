.DEFAULT_GOAL = serve

install:
	poetry install

serve:
	poetry run python3 manage.py runserver 0.0.0.0:8081

migrate:
	poetry run python3 manage.py migrate

migrations:
	poetry run python3 manage.py makemigrations

lint:
	poetry run flake8 .

test:
	poetry run python3 manage.py test
