from flask_security import RoleMixin, UserMixin
from flask_sqlalchemy import SQLAlchemy

from portal.config import configs



# THIS SHOULD SOLVE MULTIDATABASING: http://flask-sqlalchemy.pocoo.org/2.3/binds/
# Security models
class Security():

    class User(security_db.Entity, UserMixin):
        __tablename__ = "users"
        __bind_key__ = "security"
        id = PrimaryKey(int, auto=True)
        email = Required(str, 255, unique=True)
        config = Required(str, 64, unique=True)
        password = Required(str, 255)
        active = Required(bool)
        roles = Set("Role")

    class Role(security_db.Entity, RoleMixin):
        __tablename__ = "roles"
        __bind_key__ = "security"
        id = PrimaryKey(int, auto=True)
        name = Required(str, 80, unique=True)
        description = Required(str, 255)
        users = Set(User)


# Portal models
class KPMTransport():
    """
    The ORM models in use by KPM Transport
    """

    class Truck(db.Entity):
        __tablename__ = "trucks"
        __bind_key__ = "kpm_transport"
        id = PrimaryKey(int, auto=True)
        model = Required(str)

    class Employee(db.Entity):
        __tablename__ = "employees"
        __bind_key__ = "kpm_transport"
        id = PrimaryKey(int, auto=True)
        model = Required(str)


class MRTransport():
    """
    The ORM models in use by MR Transport
    """

    class Truck(db.Entity):
        __tablename__ = "trucks"
        __bind_key__ = "mr_transport"
        id = PrimaryKey(int, auto=True)
        model = Required(str)

    class Employee(db.Entity):
        __tablename__ = "employees"
        __bind_key__ = "mr_transport"
        id = PrimaryKey(int, auto=True)
        model = Required(str)


models = {
    "security": Security,
    "kpm_transport": KPMTransport,
    "mr_transport": MRTransport
}