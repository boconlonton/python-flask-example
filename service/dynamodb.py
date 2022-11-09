import boto3
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
        

    def get_all_with_pagination(self, last_evaluated_key: str=None) -> list[str]:
        pass

    def get_detail(self, id: str) -> dict[str, any]:
        products = self.dyn_resource.Table('Products')
        response = products.get_item(
            Key = {
                'pid': id
            }
        )
        product = response['Item']
        return product

    def create(self, _id, _name,_img_url, _price, _description = "No description", _material = "No Material", _specification = "No Specification", _color = "No color") -> dict[str, any]:
        products = self.dyn_resource.Table('Products')
        products.put_item(
            Item={
                'pid': _id,
                'name': _name,
                'description': _description,
                'material': _material,
                'specification': _specification,
                'color': _color,
                'img_url': _img_url,
                'price': _price
            }
        )


    def update(self, id, _name='', _img_url='', _price='', _description = '', _material = '', _specification = '', _color = '') -> dict[str, any]:
        products = self.dyn_resource.Table('Products')
        products.update_item(
            Key = {
                'pid': id,
            },
            UpdateExpression='SET #name = :name, img_url = :img_url, price = :price, description = :description, material = :material, specification = :specification, color = :color',
            ExpressionAttributeValues = {
                ':name': _name,
                ':img_url': _img_url,
                ':price': _price,
                ':description': _description,
                ':material': _material,
                ':specification': _specification,
                ':color': _color, 
            },
            ExpressionAttributeNames={
                "#name": "name"
            } 
        )


    def delete(id: str):
        pass


