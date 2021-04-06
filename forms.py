from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, IntegerField, \
    TextAreaField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class ProfessorSaveForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 250)])
    submit = SubmitField('Cadastrar')

class CursoSaveForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 250)])
    submit = SubmitField('Cadastrar')

class DisciplinaSaveForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 250)])
    submit = SubmitField('Cadastrar')

class CampusSaveForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 250)])
    submit = SubmitField('Cadastrar')

class TurmaSaveForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 250)])
    submit = SubmitField('Cadastrar')