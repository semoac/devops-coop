from flask import Blueprint, Response, render_template, jsonify, request
from .experimental import Experimental

bexp = Blueprint("experimentals", __name__, url_prefix='/experimentals')

@bexp.route('/', methods=['GET'])
def home() -> Response:
    expManager = Experimental()
    namespaces = expManager.find_namespaces()

    return render_template('experimentals.html', namespaces=namespaces)

@bexp.route('/api/namespaces', methods=['GET'])
def api_get_namespaces() -> Response:
    expManager = Experimental()
    namespaces = expManager.find_namespaces()
    return jsonify(namespaces)

@bexp.route('/api/namespaces/<ns_name>', methods=['PATCH'])
def api_patch_namespace(ns_name) -> Response:
    expManager = Experimental()
    namespace = expManager.get_namespace(ns_name)
    patched_ns = expManager.patch_namespace(namespace, request.json)
    return jsonify(patched_ns)
