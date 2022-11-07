import json


class JSONDataService:
    def connect():
        pass

    def get_all_with_pagination(last_evaluated_key: str=None) -> list[str]:
        with open('sample.json', 'r') as f:
            data = json.load(f)
        if last_evaluated_key:
            for idx, item in enumerate(data):
                if item.get('last_evaluated_key') == last_evaluated_key:
                    res = data[idx:idx+10]
        else:
            res = data[:10]
        return res

    def get_detail(id: str) -> dict[str, any]:
        pass

    def create(**kwargs) -> dict[str, any]:
        pass

    def update(**kwargs) -> dict[str, any]:
        pass

    def delete(id: str):
        pass
