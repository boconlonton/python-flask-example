import boto3
import json

# Getting credential keys
f = open('./.aws/credentials.json')
credentials = json.load(f)
ACCESS_KEY_ID = credentials['default']['aws_access_key_id']
SECRET_ACCESS_KEY = credentials['default']['aws_secret_access_key']
f.close()

# Getting configuration
f = open('./.aws/config.json')
config = json.load(f)
REGION = config['default']['region']
f.close()

client = boto3.client(
    'dynamodb',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name = REGION
)

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name = REGION
)

products = dynamodb.create_table(
    TableName = 'Products',
    KeySchema=[
        {
            'AttributeName': 'pid',
            'KeyType': 'HASH'
        },       
    ], 
    AttributeDefinitions = [
        {
            'AttributeName': 'pid',
            'AttributeType': 'N'
        },
        
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
products.wait_until_exists()

# Print out some data about the table.
print(products.item_count)



products = dynamodb.Table('Products')


# Dumb first 10 items in sample.json to DynamoDB
f = open('sample.json')
items = json.load(f)

with products.batch_writer() as batch:
    for item in items:
        batch.put_item(
            Item = {
                'pid': item['pid'],
                'name': item['name'],
                'description': item['description'],
                'material': item['material'],
                'specification': item['specification'],
                'color': item['color'],
                'img_url': item['img_url'],
                'price': item['price']
            }
        )
