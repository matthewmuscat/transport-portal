import os

from app.models import KPMEmployee, KPMTruck, MREmployee, MRTruck


class Config:
    """
    This class has the base config that goes in the flask app
    no matter what environment the flask app is created in.

    This class is only supposed to be inherited by the actual configs,
    which are sent into the app factory `create_app` to have it create
    a config with the appropriate settings.
    """

    SECRET_KEY = os.urandom(32)
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")
    PREFERRED_URL_SCHEME = "https"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # URI syntax is `provider://username:password@hostname/database`
    SQLALCHEMY_DATABASE_URI = (
        f"postgres://portal:{os.environ.get('POSTGRES_PASSWORD')}@localhost/portal"
    )


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgres:///portal"
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgres:///portal"
    LIVESERVER_TIMEOUT = 10
    SERVER_NAME = 'pytest.local'
    TESTING = True
    WTF_CSRF_ENABLED = False
    WTF_CSRF_CHECK_DEFAULT = False


# This is used to configure whose data a group can access.
# All users have a group attribute which defines which group they belong to.
model_access_perms = {
    "kpm_transport": {
        "trucks": (KPMTruck, MRTruck),
        "employees": (KPMEmployee,)
    },
    "mr_transport": {
        "trucks": (MRTruck,),
        "employees": (MREmployee,)
    }
}

# look up the config in app/__init__.py so we can apply the right one.
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
