from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.extensions import db

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')