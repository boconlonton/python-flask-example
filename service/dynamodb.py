class DynamoDBService:
    def _connect():
        pass

    def get_all_with_pagination(last_evaluated_key: str=None) -> list[str]:
        pass

    def get_detail(id: str) -> dict[str, any]:
        pass

    def create(**kwargs) -> dict[str, any]:
        pass

    def update(**kwargs) -> dict[str, any]:
        pass

    def delete(id: str):
        pass

