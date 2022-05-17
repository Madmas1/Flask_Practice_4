#===== Блюпринт main view =====#

from flask import Blueprint, render_template, request
from main.utils import search_post_by_substring
from config import POST_PATH
from functions import load_json_data
import exceptions
import logging

# Подключаем блюпринт для main view
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

# Включаем логирование
logging.basicConfig(filename="logger.log", level=logging.INFO, encoding="utf-8")


#===== Основные методы блюпринта =====#

@main_blueprint.route("/")
def main_page():
    """Метод обработки главной страницы"""
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    """Метод обработки поиска постов"""
    # Получаем от формы фразу по которой производится поиск
    s = request.args.get("s", "")
    logging.info("Производится поиск")
    # Загружаем JSON файл с постами и проверяем его на корректность
    try:
        load_posts = load_json_data(POST_PATH)
    except exceptions.DataJsonError:
        return "Загружаемый файл не является JSON файлом"
    # Ищем посты по ключевой фразе
    posts = search_post_by_substring(load_posts, s)
    # Генерируем страничку с найденными постами
    return render_template("post_list.html", posts=posts, s=s)


