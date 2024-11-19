from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from . import auth_bp
from .forms import LoginForm
from ..models import User

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, deleted=False).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard.index'))
        flash('Invalid username or password', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
