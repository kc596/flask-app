from config.factory import get_app_config
from flask import Flask
from prometheus_client import make_wsgi_app
from route.app_routes import routes
from werkzeug.middleware.dispatcher import DispatcherMiddleware


class ApplicationControllerManger:
    def __init__(self, app_name, app_routes):
        self.app = Flask(app_name)
        self.set_prometheus_route()
        self.set_application_route(app_routes)

    def set_prometheus_route(self):
        self.app.wsgi_app = DispatcherMiddleware(self.app.wsgi_app, {
            '/stats/pmetrics': make_wsgi_app()
        })

    def set_application_route(self, app_routes):
        for r in app_routes:
            self.app.add_url_rule(
                rule=r.path,
                methods=r.methods,
                view_func=r.controller)


app_config = get_app_config()
app_controller_manager = ApplicationControllerManger(app_config.name, routes)
app = app_controller_manager.app
