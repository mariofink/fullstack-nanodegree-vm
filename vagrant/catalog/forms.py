from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    category = SelectField('Category', coerce=int, validators=[DataRequired()])


class DeleteForm(FlaskForm):
    """Empty class to gain CSRF protection from FlaskForm"""
    pass
