# Stradis

Stradis é um programador de horários de cursos universitários. Construido para alocar professores e aulas em horários e, no futuro, salas de forma fácil e eficiente.

O problema de grades de horários é um assunto, fortmente pesquisado e experimentado, relacionado a instituições de ensino.

Utilizando um modelo de programação linear, esta aplicação se utiliza de informações de entrada (listas de professores, cursos, salas de aula, etc.) para criar opções de grades de horário.

## Dependências

### Resolvedor do modelo PL

O Stradis utiliza o GLPK.

### Ferramenta Web

A linguagem Python vêm instalada por padrão em diversas distribuições Linux. Caso seu sistema operacional seja diferente, deve-se encontrar uma forma de instala-lo.

Este projeto utiliza ambientes virtuais com a ferramenta [Pipenv](https://pipenv.pypa.io/en/latest/). Com python instalado, use o comando pip para instalar o Pipenv.

    pip install --user pipenv

Ao fazer o clone do repositório, navegue até a raiz do projeto e execute:

    pipenv shell

Isso criará o ambiente virtual para a instalação segura de dependencias.

Por ultimo instale as dependencias do Stradis com:

    pipenv install

## Iniciando

Com as dependencias instaladas e o ambiente virtual operante, execute:

    FLASK_APP=app.py flask run

A aplicação estará disponível na porta 5000.


