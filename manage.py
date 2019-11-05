# -*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


from flask_script import Manager
from ihome import create_app,db
from flask_migrate import Migrate,MigrateCommand

app = create_app("develop")

manage = Manager(app)

Migrate(app,db)
manage.add_command('db',MigrateCommand)






if __name__ == '__main__':
    manage.run()