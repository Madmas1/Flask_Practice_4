#===== Общие методы  =====#

from exceptions import DataJsonError
import json


def load_json_data(path):
    """Метод загрузки JSON файла с проверкой"""
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError