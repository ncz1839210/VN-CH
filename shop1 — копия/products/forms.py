from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators


class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', [validators.DataRequired()])
    stock = IntegerField('Stock', [validators.DataRequired()])
    discription = TextAreaField('Discription', [validators.DataRequired()])
    colors = TextAreaField('Discription', [validators.DataRequired()])
    
    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    #images only please is not a valid validator because it is not callable
    #image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'images only please'])
    #image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'images only please'])
    #image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'images only please'])