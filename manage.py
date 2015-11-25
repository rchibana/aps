__author__ = 'rchibana'

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand, Migrate
from app import db
from app import create_app
import os


app = create_app()

migrate = Migrate(app, db)

manager = Manager(app)

PORT = os.environ.get('PORT', 5000)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=PORT))

if __name__ == '__main__':
    manager.run()
