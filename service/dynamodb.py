import boto3
from boto3.dynamodb.conditions import Key, Attr
import json

class DynamoDBService:
    def __init__(self):
        '''
        Init an instance of dynamoDB client and resource
        '''

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

        dyn_client = boto3.client(
            'dynamodb',
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=SECRET_ACCESS_KEY,
            region_name = REGION
        )

        dyn_resource = boto3.resource(
            'dynamodb',
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=SECRET_ACCESS_KEY,
            region_name = REGION
        )

        self.dyn_client = dyn_client,
        self.dyn_resource = dyn_resource
        

    def _connect():
        pass
        
    def get_all_item(self):
        products = self.dyn_resource.Table('Products')
        response = products.scan()
        items = response['Items']
        return items


    def get_all_with_pagination(self, last_evaluated_key: str=None) -> list[str]:
        products = self.dyn_resource.Table('Products')
        response = products.scan(
            Limit=10,
            ExclusiveStartKey=last_evaluated_key
        )
        items = response['Items']
        return items


    def get_detail(self, id: str) -> dict[str, any]:
        products = self.dyn_resource.Table('Products')
        response = products.get_item(
            Key = {
                'pid': id
            }
        )
        product = response['Item']
        return product

    def create(self, **kwargs) -> dict[str, any]:
        products = self.dyn_resource.Table('Products')
        products.put_item(
            Item={
                'pid': kwargs['id'],
                'name': kwargs['name'],
                'description': kwargs['description'],
                'material': kwargs['material'],
                'specification': kwargs['specification'],
                'color': kwargs['color'],
                'price': kwargs['price']
            }
        )


    def update(self, id, **kwargs) -> dict[str, any]:
        products = self.dyn_resource.Table('Products')
        products.update_item(
            Key = {
                'pid': id,
            },
            UpdateExpression='SET #name = :name, description = :description, material = :material, specification = :specification, color = :color, price = :price',
            ExpressionAttributeValues = {
                ':name': kwargs['name'],
                ':description': kwargs['description'],
                ':material': kwargs['material'],
                ':specification': kwargs['specification'],
                ':color': kwargs['color'], 
                ':price': kwargs['price'],
            },
            ExpressionAttributeNames={
                "#name": "name"
            } 
        )


    def delete(self, id):
        products = self.dyn_resource.Table('Products')
        products.delete_item(
            Key = {
                'pid': id
            }
        )
