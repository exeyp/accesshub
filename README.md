export FLASK_CONFIG=config.DevelopmentConfig

export FLASK_CONFIG=config.ProductionConfig

gunicorn -w 4 -b 127.0.0.1:8000 run:app

#Процесс миграций
Переменная окружения FLASK_APP указывает Flask, где искать главный файл приложения, из которого будет запускаться сервер.
export FLASK_APP=run.py 

flask db init — Создаёт инфраструктуру для миграций (только один раз в начале).
flask db migrate -m "Initial migration" — Создаёт новые файлы миграций на основе изменений в моделях данных.
flask db upgrade — Применяет миграции, синхронизируя структуру базы данных с моделями.