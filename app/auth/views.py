from flask import render_template, redirect, url_for, flash
from . import auth_bp
from .forms import LoginForm
from ..models import User

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Выполнение логики аутентификации пользователя
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash('Вы успешно вошли!', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('Неверное имя пользователя или пароль', 'danger')
    return render_template('auth/login.html', form=form)
