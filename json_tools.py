import json

# Accesses a json file and returns it as a dict
def get_dict(filepath: str) -> dict:
    try:
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File {filepath} not found")
        return {}
    
def update_json(dictionary: dict, json_path: str) -> None:
    try:
        with open(json_path, 'w') as json_file:
            json.dump(dictionary, json_file, indent=4)
    except FileNotFoundError:
        print(f"File {json_path} not found")