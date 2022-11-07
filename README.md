# python-flask-example

### Installation

- Install virtual environment
```
pip install virtualenv
```
- Create & active virtual environment
```
virtualenv .venv && source .venv/bin/activate
```
- Install dependencies
```
pip install -r requirements.txt
```
- Run the app
```
export FLASK_APP=app
export FLASK_ENVIRONMENT=development
flask run
```