import os
import click
from app import create_app, db
from flask_migrate import Migrate


# Считываем переменную окружения для типа конфигурации
config = os.getenv('FLASK_CONFIG', 'config.DevelopmentConfig')

app = create_app(config)

migrate = Migrate(app, db)

@app.cli.command("init-db")
def initialize_database():
    """Initialize the database with initial data."""
    with app.app_context():
        from app.models import init_db
        init_db()
        click.echo("Database initialized. Tables created and initial data added.")