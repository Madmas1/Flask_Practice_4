#====== Основной скрипт приложения ======#

from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

#====== Подключение блюпринтов проекта ======#

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


# Роут на выгрузку файлов из каталога
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

# Запуск приложения
if __name__ == "__main__":
    app.run()

