from flask import Blueprint

from .. import models

auth_bp = Blueprint('auth', __name__)

from . import views
