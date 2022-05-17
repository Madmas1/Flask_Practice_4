#===== Блюпринт loader view =====#

from flask import Blueprint, render_template, request
from loader.utils import save_picture, add_new_post
from exceptions import WrongImgType
import logging

# Подключаем блюпринт для loader view
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")

# Включаем логирование
logging.basicConfig(filename="logger.log", level=logging.INFO, encoding="utf-8")

#===== Основные методы блюпринта =====#

@loader_blueprint.route("/post", methods=["GET"])
def create_new_post_page():
    """ Метод для отображения формы с созданием поста"""
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def create_new_post_by_user():
    """ Метод на создание нового поста """
    # Запросы на данные получаемые в форме
    picture = request.files.get("picture")
    content = request.form.get("content")
    # Проверка контента на наличие данных
    if not picture or not content:
        logging.info("Данные не загружены, отсутствует часть данных")
        return "Отсутствует часть данных"
    # Сохранение изображения и проверка на формат файла
    try:
        picture_path = save_picture(picture)
    except WrongImgType:
        return "Неверный формат изображения"
    # Создание нового поста
    new_post = add_new_post(picture_path, content)
    # Генерируем страничку с результатами загрузки поста
    logging.info("Добавлен новый пост")
    return render_template("post_uploaded.html", new_post=new_post)
