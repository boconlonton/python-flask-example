import json

import uuid

from faker import Faker

import faker_commerce

list_specification = []

fake = Faker()
fake.add_provider(faker_commerce.Provider)

with open('sample.json', 'w+') as f:
    data = []
    for i in range(100):
        product = {
            'pid': i,
            'name': fake.ecommerce_name(),
            'description': fake.text(),
            'material': fake.ecommerce_category(),
            'specification': '12 x 12',
            'color': fake.color_name(),
            'img_url': fake.image_url(),
            'price': fake.ecommerce_price(),
            'last_evaluated_key': str(uuid.uuid4())
        }
        data.append(product)
    json.dump(data, f)
