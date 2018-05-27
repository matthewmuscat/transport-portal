import os

from flask_migrate import Migrate, migrate, upgrade

from app import RouteManager

# Set up the route manager with the correct config
if "FLASK_DEBUG" in os.environ:
    manager = RouteManager("development")
else:
    manager = RouteManager("production")

app = manager.app
db = manager.db

# Migrate and create tables
Migrate(app, db)
with app.app_context():
    migrate()
    upgrade()

# Should we auto reload when templates change?
if app.config['TEMPLATES_AUTO_RELOAD']:
    app.jinja_env.auto_reload = True

# Start the app!
if __name__ == '__main__':
    app.run()
