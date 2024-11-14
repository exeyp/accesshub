import os
from app import create_app, db
from flask_migrate import Migrate


# Считываем переменную окружения для типа конфигурации
config = os.getenv('FLASK_CONFIG', 'config.DevelopmentConfig')

# Создаем экземпляр приложения Flask
app = create_app(config)

# Инициализируем Flask-Migrate для управления миграциями
migrate = Migrate(app, db)
