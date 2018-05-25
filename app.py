import os

from portal.route_manager import RouteManager

manager = RouteManager()
app = manager.app

debug = os.environ.get('FLASK_DEBUG')
if debug:
    app.jinja_env.auto_reload = True

if __name__ == '__main__':
    manager.run()
