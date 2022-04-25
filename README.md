# A sample application with known vulnerabilities - Python, Django

A sample application with known issues for testing various linters, scanners,
and scan automation.

This project uses:

| Component   | In Use                                   | 
|-------------|------------------------------------------|
| Platform    | [Python](https://www.python.org/)        |
| Language(s) | [Python](https://www.python.org/)        |
| Build       | [Poetry](https://python-poetry.org/)     |
| Framework   | [Django](https://www.djangoproject.com/) |

## Security issues

| Vulnerability Type | Description | Location | PoC Command |
|--------------------|-------------|----------|-------------|
| --                 | --          | --       | --          |

### Other issues

* The project has no tests

## Running this code

**NOTE: This project contains security vulnerabilities and should be only run in
testing purposes.**

Requirements:

* [Poetry](https://python-poetry.org/docs/#installation)
* [Python 3.8](https://www.python.org/downloads/)

To run the code locally:

```shell
# Clone the project
git clone https://github.com/the-scan-project/tsp-vulnerable-app-python-django.git 
cd tsp-vulnerable-app-python-django

# Install package dependencies (django, etc)
poetry install

# Run database migrations (No changes detected in app 'hello')
poetry run python manage.py makemigrations hello

# Supply environment variables
export ALLOWED_HOSTS=0.0.0.0
export SECRET_KEY=example-secret-key
export DEBUG=True

# Start the application
poetry run python manage.py runserver 0.0.0.0:8080
```
