from werkzeug import secure_filename
from flask_wtf.file import FileField
from flask.ext.wtf import Form
from wtforms import SubmitField

class ClientForm(Form):
    filename=FileField('add photo')
    submit=SubmitField("Send for processing")
