# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

# Пример

class Config(object):
    DEBUG = True
    SECRET_HERE = 'dasdasdsadasda'
    #SECRET_HERE = 'dasdasdsadasda'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory.db:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 3}
