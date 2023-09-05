from flask import Blueprint
from .views import index

bp = Blueprint("webui", __name__, template_folder="templates",
    url_prefix=""
)

bp.add_url_rule('/', view_func=index, endpoint="index", methods=["POST", "GET"])


def init_app(app):
    app.register_blueprint(bp)