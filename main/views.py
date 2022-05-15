from flask import Blueprint, render_template, request
import logging
from main.utils import *


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logger.log", level=logging.INFO, encoding="utf-8")


@main_blueprint.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    s = request.args.get("s", "")
    logging.info("Производится поиск")
    load_posts = load_json_data("./posts.json")
    posts = search_post_by_substring(load_posts, s)
    return render_template("post_list.html", posts=posts, s=s)


