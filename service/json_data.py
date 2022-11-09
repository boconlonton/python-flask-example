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


    def get_detail(id: int) -> dict[str, any]:
        with open('sample.json', 'r') as f:
            data = json.load(f)
        for item in data:
            if item['pid'] == id:
                return item
        return None


    def create(**kwargs) -> dict[str, any]:
        with open('sample.json', 'r') as f:
            data = json.load(f)
        idx = len(data)
        new_item = {
            'pid': idx,
            **kwargs
        }
        data.append(new_item)
        with open('sample.json', 'w') as g:
            json.dump(data, g)
        return new_item


    def update(id: int, **kwargs) -> dict[str, any]:
        updated_item = None
        with open('sample.json', 'r') as f:
            data = json.load(f)
            for idx, item in enumerate(data):
                if item['pid'] == id:
                    updated_item = {
                        **item,
                        **kwargs
                    }
                    data[idx] = updated_item
        if updated_item:
            with open('sample.json', 'w') as g:
                json.dump(data, g)
        return updated_item


    def delete(id: int) -> None:
        with open('sample.json', 'r') as f:
            data = json.load(f)
        new_data = list(filter(lambda x: x['pid'] != id, data))
        with open('sample.json', 'w') as g:
                json.dump(new_data, g)
