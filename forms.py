from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class IndexForm(FlaskForm):
    personal = StringField('Personal', validators=[DataRequired()])
    mes = StringField('Mes', validators=[DataRequired()])
    anio = StringField('Anio', validators=[DataRequired()])
    submit = SubmitField('Imprimir')


