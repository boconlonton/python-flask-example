from .dynamodb import DynamoDBService
from .json_data import JSONDataService


class Factory:

    def get(use_dynamo=False, *args, **kwargs):
        if use_dynamo:
            return DynamoDBService
        else:
            return JSONDataService
