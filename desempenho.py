from app.desempenho_case import gerar
from app import create_app
from app.extensions import db, csrf, migrate
from faker import Faker

app = create_app()
ctx = app.app_context()
fake = Faker('pt_BR')
ctx.push()

for i in range(50):

    print('---------------------------------- Interação ' + str(i) + ' ----------------------------------')

    db.drop_all()
    db.create_all()
    gerar(
        fake.random_int(40, 60),
        fake.random_int(50, 70),
        fake.random_int(8, 10),
    )

    print('---------------------------------- Interação ' + str(i) + ' ----------------------------------')
    print('')
    print('')

ctx.pop()
