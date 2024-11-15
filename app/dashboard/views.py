from flask import render_template
from . import dashboard_bp
from flask_login import login_required

@dashboard_bp.route('/')
@login_required
def index():
    return render_template('dashboard/index.html')
