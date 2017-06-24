from flask import Flask, render_template
from wtforms import Form, StringField, PasswordField


app = Flask("FlaskProject")
app.debug = True


@app.route('/', methods=('GET', 'POST'))
def submit():
    form = FormPassword()
    return render_template('form.html', form=form)


class FormPassword(Form):
    site = StringField('Site')
    username = StringField('User Name')
    email = StringField('Email')
    password = PasswordField('Passaword')

if __name__ == '__main__':
    app.run()
