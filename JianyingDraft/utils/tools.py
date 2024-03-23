import os
import shutil
import uuid
import json


def generate_id():
    """
        生成uuid
    """
    return str(uuid.uuid4()).upper()


def write_json(path, data):
    with open(path, 'w') as file:
        json.dump(data, file)
    pass


def read_json(path):
    with open(path, 'r') as file:
        return json.load(file)
    pass


def create_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    pass

    os.mkdir(folder_path)





