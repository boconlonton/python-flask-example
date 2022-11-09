from flask import Flask, render_template, request, redirect, url_for

from flask_wtf.csrf import CSRFProtect

from service import Factory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'w=>FV&0F|1R^jx,~f0$&ci>w-4C?tp'

csrf = CSRFProtect()
csrf.init_app(app)

service = Factory.get(use_dynamo=False)


@app.route('/')
def index():
    products = service.get_all_with_pagination()

    return render_template('index.html', products=products)


@app.route('/<int:prod_id>')
def details(prod_id):
    product = service.get_detail(id=prod_id)
    if product:
        return render_template('detail.html', product=product)
    else:
        return 'NOT FOUND'


@app.route('/update/<int:prod_id>', methods=['GET', 'POST'])
def update(prod_id):
    if request.method == 'POST':
        product = {
            'name': request.form['productName'],
            'description': request.form['description'],
            'material': request.form['material'],
            'specification': request.form['specification'],
            'color': request.form['color'],
            'price': int(request.form['price'])
        }
        service.update(id=prod_id, **product)
        return redirect(url_for('update', prod_id=prod_id))
    else:
        product = service.get_detail(id=prod_id)
    return render_template('form.html', product=product)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        product = {
            'name': request.form['productName'],
            'description': request.form['description'],
            'material': request.form['material'],
            'specification': request.form['specification'],
            'color': request.form['color'],
            'price': request.form['price']
        }
        prod = service.create(**product)
        return redirect(url_for('details', prod_id=prod['pid']))
    return render_template('form.html', product=None)

@app.route('/delete/<int:prod_id>')
def delete(prod_id):
    service.delete(id=prod_id)
    return redirect(url_for('index'))
