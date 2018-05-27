from os import environ

from flask_migrate import Migrate, migrate, upgrade

from app.route_manager import RouteManager

# Set up the app and the database
manager = RouteManager()
app = manager.app
db = manager.db
Migrate(app, db)

# Migrate and create tables
with app.app_context():
    migrate()
    upgrade()

# If we're in debug mode, auto reload whenever there's a change to a file.
debug = environ.get('TEMPLATES_AUTO_RELOAD', None)
if debug:
    app.jinja_env.auto_reload = True

if __name__ == '__main__':
    manager.run()
