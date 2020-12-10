from flask import Blueprint

api = Blueprint('base_bp', __name__)


from .template_controller import *
from .user_controller import *
