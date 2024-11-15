from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Модель роли
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), unique=True, nullable=False)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    full_name = db.Column(db.String(64), nullable=True)
    phone = db.Column(db.String(11), nullable=True)
    deleted = db.Column(db.Boolean, default=False)
    reg_date = db.Column(db.DateTime, nullable=False)

    role = db.relationship('Role', backref=db.backref('users', lazy=True))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Заполнение базы данных ролями и пользователем admin
def init_db():
    db.create_all()

    # Проверка наличия ролей
    if not Role.query.filter_by(title='admin').first():
        admin_role = Role(title='admin')
        user_role = Role(title='user')
        db.session.add(admin_role)
        db.session.add(user_role)
        db.session.commit()

    # Заполнение таблицы пользователей
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', role_id=1, reg_date=datetime.utcnow())
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()
