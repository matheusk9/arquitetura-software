import click
from projetoFlask.ext.database import db
from projetoFlask.ext.auth import create_user
from projetoFlask.ext.database import TypeUsers, ListUsers


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def new_name(pessoa):
    new_user = ListUsers(
            # id=1, 
            name=pessoa, 
    )
    db.session.bulk_save_objects(new_user)
    db.session.commit()
    return ListUsers.query.all()


def populate_db():
    """Populate db with sample data"""
    tp = [
            TypeUsers(
                id=1,
                ),
            TypeUsers(
                id=2,
                )
        ]

    data = [
        tp[0],
        tp[1],
        ListUsers(
            id=1, 
            name="Usuario 1", 
            type_id=tp[0].id),
        ListUsers(
            id=2, 
            name="Usuario 2", 
            type_id=tp[0].id),
        ListUsers(
            id=3, 
            name="Usuario 3", 
            type_id=tp[1].id),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return ListUsers.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)