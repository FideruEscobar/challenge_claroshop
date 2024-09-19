import os, json
from flask import jsonify
from datetime import datetime



def output_json(data: dict):
    return jsonify(data)


def date_to_datetime(date: str) -> datetime:
    d = datetime.strptime(date, '%Y-%m-%d')
    return d

def open_json(current_dir, filename: str):
    file_path= os.path.join(current_dir, filename)
    with open(file_path, 'r') as f:
        return json.load(f)