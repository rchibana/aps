__author__ = 'rchibana'

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand, Migrate
from app import db
from app import create_app
import os

app = create_app()

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(port=os.environ.get('$PORT'))
