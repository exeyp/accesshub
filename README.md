python -m venv .venv
pip freeze > requirements.txt
pip install -r requirements.txt

export FLASK_CONFIG=config.DevelopmentConfig
export FLASK_CONFIG=config.ProductionConfig

gunicorn -w 4 -b 0.0.0.0:8000 run:app
gunicorn -w 1 -b localhost:8000 run:app

Flask CLI автоматически ищет приложение по имени в переменной окружения FLASK_APP. Если переменная FLASK_ENV=development, сервер запускается в режиме отладки.

export FLASK_APP=run.py
export FLASK_ENV=development #Автоперезагрузка активна. DEBUG автоматически включён.

flask run --host=0.0.0.0 --port=8000
flask run --host=localhost --port=8000

#Процесс миграций

flask db init — Создаёт инфраструктуру для миграций (только один раз в начале).
flask db migrate -m "Initial migration" — Создаёт новые файлы миграций на основе изменений в моделях данных. Используется для внесения изменений в структуру базы данных без потери данных
flask db upgrade — Применяет миграции, синхронизируя структуру базы данных с моделями.


#ToDo
1. Вынести зависимости из run.py и app/__init__.py:
Например, создать модуль commands.py для всех пользовательских CLI-команд.
2. Улучшить обработку переменных окружения:
Используйте библиотеку python-dotenv для удобного управления переменными окружения.
3. Добавить настройки логирования:
Для мониторинга ошибок и запросов в продакшене.