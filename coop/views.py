from flask import Blueprint, Response, render_template

from .client import k8s_client

bexp = Blueprint("experimentals", __name__, url_prefix='/experimentals')

NAMESPACES_LABEL_SELECTOR='enviroment=experimental'

@bexp.route('/', methods=['GET'])
def home() -> Response:
    #namespaces = list_namespaces(NAMESPACES_LABEL_SELECTOR)

    namespaces = []
    if len(namespaces) == 0:
        return render_template('experimentals.html', entries=[])
