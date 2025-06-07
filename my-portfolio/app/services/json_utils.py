def read_json_file(file_path: str):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def append_to_json_file(file_path: str, new_data: dict):
    data = read_json_file(file_path)
    data.append(new_data)
    write_json_file(file_path, data)

def update_json_file(file_path: str, updated_data: dict, identifier: str):
    data = read_json_file(file_path)
    for index, item in enumerate(data):
        if item['id'] == identifier:
            data[index] = updated_data
            break
    write_json_file(file_path, data)

def delete_from_json_file(file_path: str, identifier: str):
    data = read_json_file(file_path)
    data = [item for item in data if item['id'] != identifier]
    write_json_file(file_path, data)