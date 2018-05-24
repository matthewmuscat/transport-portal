import os

from flask import Flask, render_template
from flask_security import PonyUserDatastore, RoleMixin, Security, UserMixin, login_required
from pony.orm import Database, PrimaryKey, Required, Set

app = Flask(__name__)
db = Database()

# MOVE ALL THIS TO A CONFIG OBJECT #
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT")

PSQL_USER = os.environ.get("PSQL_USER")
PSQL_HOST = os.environ.get("PSQL_HOST")
PSQL_PASS = os.environ.get("PSQL_PASS")
PSQL_DB = os.environ.get("PSQL_DB")


# MOVE ALL THIS TO MODELS.PY LATER
class User(db.Entity, UserMixin):
    id = PrimaryKey(int, auto=True)
    email = Required(str, 255, unique=True)
    password = Required(str, 255)
    active = Required(bool)
    roles = Set('Role')


class Role(db.Entity, RoleMixin):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 80, unique=True)
    description = Required(str, 255)
    users = Set(User)


db.bind(
    provider='postgres',
    user=PSQL_USER,
    password=PSQL_PASS,
    host=PSQL_HOST,
    database=PSQL_DB,
)

db.generate_mapping()

# Set up Flask-Security
user_datastore = PonyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create a user to test with
# @app.before_first_request
# def create_user():
#    user_datastore.create_user(email="lemon@pydis.com", password="test")
#    db.commit()


@app.route("/")
@login_required
def hello():
    return render_template("under_construction.html")
