install:
	poetry install

serve:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

lint:
	poetry run flake8 .
