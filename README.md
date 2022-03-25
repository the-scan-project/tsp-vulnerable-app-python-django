# A sample application with known vulnerabilities - Python, Django

A sample application with known issues for testing various linters, scanners,
and scan automation.

This project uses:

| Component   | In Use                                   | 
|-------------|------------------------------------------|
| Platform    | Python                                   |
| Language(s) | [Python](https://www.python.org/)        |
| Build       | [Poetry](https://python-poetry.org/)     |
| Framework   | [Django](https://www.djangoproject.com/) |

## Security issues

| Vulnerability Type                                                               | Description                                                                                                                                                                      | Location                                                                            | Poc Command                                                          |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [Cross Site Scripting (XSS)](https://cwe.mitre.org/data/definitions/79.html)     | `hello.views.index` generates page output in code. It expects a name as a parameter to say `f"Hello, {name}"` and just interpolates user input to the output without escaping it | `return HttpResponse(f"Hello, {name}")`                                             | <http://localhost:8000/hello?name=%3Cscript%3Ealert(1)%3C/script%3E> | 
| [Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html) | There are secrets in the code committed to the repository                                                                                                                        | `SECRET_KEY = "django-insecure-$^e#o&rg#c$)114)g!mgn=b_#$8n5hsma2r7xoaf-%-0o^ei4g"` | N/A                                                                  |

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

# Start the application
poetry run python manage.py runserver
```
