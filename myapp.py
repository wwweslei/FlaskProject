from flask import Flask, render_template, flash
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from datetime import datetime


app = Flask("FlaskProject")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ImU4MjczZmFhMzkZWUzMT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
app.debug = True


@app.route('/', methods=('GET', 'POST'))
def password_form():
    form = FormPassword()
    formSearch = FormSearch()
    model = db_sites
    if form.validate_on_submit():
        db.session.add(model(form.site.data, form.username.data,
                             form.email.data, form.password.data))
        try:
            db.session.commit()
            flash("Seus dados foram salvos")
        except:
            flash("Site já registrado")
    elif formSearch.validate_on_submit():
        _requests = formSearch.siteSearch.data
        search_model = model.query.filter_by(db_site=_requests).first()
        return render_template('index.html', form=form, formSearch=formSearch,
                               resp_model=search_model)

    return render_template('form.html', form=form, formSearch=formSearch)


class FormSearch(FlaskForm):
    siteSearch = StringField('Site', validators=[DataRequired()])


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

    def __getitem__(self, position):
        self.lista = [self.db_site, self.db_username, self.db_email,
                      self.db_password, self.db_date]
        return self.lista[position]


if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0")
