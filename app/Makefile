install:
	pip install -r requirements.txt

setup-db:
	flask db init
	flask db migrate -m "Initial migration"
	flask db upgrade