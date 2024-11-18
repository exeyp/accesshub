from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

# Role model
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), unique=True, nullable=False)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    full_name = db.Column(db.String(64), nullable=True)
    phone = db.Column(db.String(11), nullable=True)
    deleted = db.Column(db.Boolean, default=False)
    reg_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    role = db.relationship('Role', backref=db.backref('users', lazy=True))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def active_users():
        return User.query.filter_by(deleted=False)

# Database initialization
def init_db():
    db.create_all()

    # Add roles
    admin_role = Role.query.filter_by(title='admin').first()
    user_role = Role.query.filter_by(title='user').first()
    if not admin_role:
        admin_role = Role(title='admin')
        db.session.add(admin_role)
    if not user_role:
        user_role = Role(title='user')
        db.session.add(user_role)
    db.session.commit()

    # Add admin user
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', role=admin_role)
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()
