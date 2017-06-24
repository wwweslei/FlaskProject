from flask import Flask, render_template
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


app = Flask("FlaskProject")
app.config['SECRET_KEY'] = 'ImU4MjczZmFhMzkZWUzMT'
app.debug = True


@app.route('/', methods=('GET', 'POST'))
def submit():
    form = FormPassword()
    if form.validate_on_submit():
        print(form.data)
    else:
        print(form.errors)
    return render_template('form.html', form=form)


class FormPassword(FlaskForm):
    site = StringField('Site', validators=[DataRequired()])
    username = StringField('User Name')
    email = StringField('Email')
    password = PasswordField('Passaword', validators=[DataRequired()])

if __name__ == '__main__':
    app.run()
