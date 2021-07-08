import os
import uuid
import click

from flask import Flask, render_template, flash, redirect, url_for, request
from flask_migrate import Migrate
from forms import *
from models import *

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/stradis"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

migrate = Migrate(app, db)

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_errors(app)
    register_commands(app)
    register_shell_context(app)
    register_filters(app)

    return app

def register_extensions(app):
    db.init_app(app)
    babel.init_app(app)
    csrf.init_app(app)

def register_blueprints(app):
    app.register_blueprint(titulo_bp, url_prefix='/titulos')

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

def register_commands(app):
    """
        Command line functions
    """
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, Titulo=Titulo)

def register_filters(app):
    @app.template_filter()
    def format_date(value):
        return flask_babel.format_date(value, 'short')

    @app.template_filter()
    def format_currency(value):
        return flask_babel.format_currency(value, 'BRL')