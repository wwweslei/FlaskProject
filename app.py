from flask import Flask, render_template, flash
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask("FlaskProject")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ImU4MjczZmFhMzkZWUzMT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.debug = True
db = SQLAlchemy(app)


@app.route('/', methods=('GET', 'POST'))
def password_form():
    form = FormPassword()
    model = db_sites
    if form.validate_on_submit():
        db.session.add(model(form.site.data, form.username.data,
                             form.email.data, form.password.data))
        db.session.commit()
        flash("Dados salvos com sucesso")
    else:
        forms = [x.data for x in form]
        print(forms)
        print(type(form))
        # print(form.errors)
    return render_template('form.html', form=form)


class FormPassword(FlaskForm):
    site = StringField('Site', validators=[DataRequired()])
    username = StringField('User Name')
    email = StringField('Email')
    password = PasswordField('Passaword', validators=[DataRequired()])


class db_sites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db_site = db.Column(db.String(20), unique=True)
    db_username = db.Column(db.String(20))
    db_email = db.Column(db.String(20))
    db_password = db.Column(db.String(100))
    db_date = db.Column(db.DateTime)

    def __init__(self, site, username, email, password):
        self.db_site = site
        if username:
            self.db_username = username
        else:
            self.db_username = "wwweslei"
        if email:
            self.db_email = email
        else:
            self.db_email = "www.weslei@gmail.com"
        self.db_password = password
        self.db_date = datetime.utcnow()

    def __repr__(self):
        return '<DB Site %r>' % self.site


if __name__ == '__main__':
    app.run()
