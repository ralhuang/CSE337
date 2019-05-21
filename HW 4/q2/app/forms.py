from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Required

class SubmissionForm(FlaskForm):
    title = StringField('Submit new Text')
    text = TextAreaField('Text', validators=[DataRequired()])
    radio1 = RadioField('Choices', choices=[('wordcount', 'Word Count'), ('charactercount', 'Character Count'), ('5mostfrequent', 'Most Frequent 5 Words')], default='wordcount')
    delimtext = StringField('Delimiters: ')
    submit = SubmitField('Submit Text')

