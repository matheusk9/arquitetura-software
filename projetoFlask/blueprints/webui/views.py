from flask import abort, render_template, request
from projetoFlask.ext.database import ListUsers, db
from projetoFlask.ext.commands import new_name

def index():
    users = ListUsers.query.all()
    if request.method == 'POST':
        user_name = request.form.get('name')
        novo = ListUsers(name=user_name)
        db.session.add(novo)
        db.session.commit()
    users = ListUsers.query.all()
    return render_template("index.html", users=users)
