from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class):
    # Создаем экземпляр приложения Flask
    app = Flask(__name__)

    # Загрузка конфигурации из класса
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрация Blueprints
    from app.auth import auth_bp
    from app.dashboard import dashboard_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    return app
