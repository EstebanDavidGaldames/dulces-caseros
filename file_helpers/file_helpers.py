import json


def write_json_file(path:str, element:list[dict] = []) -> None:
    with open(path, 'w') as file:
        json.dump(element, file, indent=4)


def read_json_file(path) -> list[dict]:
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        write_json_file(path)
