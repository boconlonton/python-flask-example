from .dynamodb import DynamoDBService
from .json_data import JSONDataService


class Factory:

    def get(use_dynamo=True, *args, **kwargs):
        if use_dynamo:
            dynamodbService = DynamoDBService()
            return dynamodbService
        else:
            return JSONDataService
