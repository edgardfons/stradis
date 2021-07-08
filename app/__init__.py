import os

from flask import Flask, render_template

from app.extensions import db, csrf, migrate
from app.settings import config
from app.blueprints.curso import curso_bp
from app.blueprints.professor import professor_bp

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_errors(app)

    return app

def register_extensions(app):
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    app.register_blueprint(curso_bp, url_prefix='/cursos')
    app.register_blueprint(professor_bp, url_prefix='/professores')

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors.html', code=400, info='Bad Request'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors.html', code=403, info='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors.html', code=404, info='Page Not Found'), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('errors.html', code=405, info='The method is not allowed for the requested URL.'), 405

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors.html', code=500, info='Server Error'), 500