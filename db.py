from myapp import db, db_sites


banco = db_sites
# me = banco("fffffflllllfffff", "dlisadhodui", "dsoaihpgi", 'ihogo')
# db.session.add(me)
# db.session.commit()
p = banco.query.filter_by(db_site='vivo').first()
# print(p.db_site, p.db_password, p.db_username, p.db_email, p.db_date, p.id)
for x in p:
    print(x)
print(p[0])