import os


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

    # This is used to configure whose data a user can access.
    MODEL_ACCESS_PERMISSIONS = {
        "kpm_transport": {
            "trucks": ("kpm_transport", "mr_transport"),
            "employees": ("kpm_transport",)
        },
        "mr_transport": {
            "trucks": ("mr_transport",),
            "employees": ("mr_transport",)
        }
    }


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    LIVESERVER_TIMEOUT = 10
    SERVER_NAME = 'pytest.local'
    TESTING = True
    WTF_CSRF_ENABLED = False
    WTF_CSRF_CHECK_DEFAULT = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgres:///portal"
    )


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
