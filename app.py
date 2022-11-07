from flask import Flask, render_template

from service import Factory

app = Flask(__name__)

@app.route('/')
def index():
    service = Factory.get(use_dymano=False)
    products = service.get_all_with_pagination()

    return render_template('index.html', products=products)