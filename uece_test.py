from app.uece_case import gerar
from app import create_app
from app.extensions import db, csrf, migrate

app = create_app()
ctx = app.app_context()
ctx.push()

db.drop_all()
db.create_all()

gerar()

ctx.pop()
