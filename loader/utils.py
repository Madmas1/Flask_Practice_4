#===== Методы для обработки loader view =====#

from functions import load_json_data
from config import UPLOAD_FOLDER, POST_PATH
from exceptions import WrongImgType
import json


def save_picture(picture):
    """ Метод сохраняющий изображения"""
    # Определяем допускаемые форматы файлов и определяем тип файла
    allowed_types = ['jpg', 'png', 'gif', 'jpeg']
    picture_type = picture.filename.split('.')[-1]
    # Проверяем формат файла
    if picture_type not in allowed_types:
        raise WrongImgType(f"Неверный формат файла. Допускаются следующие форматы файлов: {', '.join(allowed_types)}")
    # Сохраняем файл
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    # Возвращаем путь до файла для дальнейшей обработки
    return picture_path


def add_new_post(picture_path, content):
    """ Метод добавляющий новый пост"""
    # Загружаем JSON файл с контентом постов
    posts = load_json_data(POST_PATH)
    # Определяем словарь с данными нового поста
    new_post = {"pic": picture_path, "content": content}
    # Добавляем новый пост и сохраняем его в JSON файл
    posts.append(new_post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)
    # Возвращаем данные о новом посте для дальнейшей обработки
    return new_post