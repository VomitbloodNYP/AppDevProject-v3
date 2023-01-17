from wtforms import Form, validators, IntegerField, StringField

class EditPackForm(Form):
    pack_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    pack_count = IntegerField('', [validators.NumberRange(min=1, max=150), validators.DataRequired()], default=0)
    pack_price = IntegerField('', [validators.NumberRange(min=1, max=150), validators.DataRequired()], default=0)
