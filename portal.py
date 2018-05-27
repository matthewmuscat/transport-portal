import os

from flask_migrate import Migrate, migrate, upgrade

from app import create_app, db
from app.route_manager import RouteManager

# Set up the app and the database
if "FLASK_DEBUG" in os.environ:
    app = create_app("development")
else:
    app = create_app("production")

# Set up the app and the database
manager = RouteManager(app, db)
Migrate(app, db)

# Migrate and create tables
with app.app_context():
    migrate()
    upgrade()

# Should we auto reload when templates change?
if app.config['TEMPLATES_AUTO_RELOAD']:
    app.jinja_env.auto_reload = True

# Start the app!
if __name__ == '__main__':
    manager.run()
