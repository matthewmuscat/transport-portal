import os

from alembic.util.exc import CommandError
from flask_migrate import Migrate, init, migrate, upgrade

from app import RouteManager

# Set up the route manager with the correct config
if "FLASK_DEBUG" in os.environ:
    manager = RouteManager("development")
else:
    manager = RouteManager("production")

app = manager.app
db = app.db

# Migrate and create tables
Migrate(app, db)
with app.app_context():
    try:
        upgrade()  # Make sure the database is up to date.
        migrate()  # Make any migrations that might be necessary.
        upgrade()  # Apply the new migration, if one was made.
    except CommandError as e:

        if "Please use the 'init' command" in str(e):
            init()  # Gotta set up migrations first.

# Should we auto reload when templates change?
if app.config['TEMPLATES_AUTO_RELOAD']:
    app.jinja_env.auto_reload = True

# Start the app!
if __name__ == '__main__':
    app.run()
