#===== Классы обработчиков исключений =====#


# Обработчик исключения для JSON файла
class DataJsonError(Exception):
    pass


# Обработчик исключения для типов загружаемых файлов
class WrongImgType(Exception):
    pass