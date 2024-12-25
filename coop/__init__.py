from flask import Flask, jsonify, Response
import os



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, static_folder=os.path.dirname(
        os.path.abspath(__file__)) + '/static',
        template_folder='templates')
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/healthz')
    def healthz():
        return jsonify({}), 200
    from . import views
    app.register_blueprint(views.bexp)

    return app

