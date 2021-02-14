class Route:
    """
    A route object defines an endpoint of the application.

    :param path: a string used to register path of url which invokes given controller
    :param methods: an array of string defining allowed HTTP methods for the endpoint
    :param controller: the method which will be invoked
    """

    def __init__(self, path, methods, controller):
        self.path = path
        self.methods = methods
        self.controller = controller

    def register(self, wsgi_app):
        """
        Registers this route to external wsgi_app - Flask.

        :param wsgi_app: The flask app object that will register this endpoint.
                            wsgi_app = Flask('yourapplication')
        """
        wsgi_app.add_url_rule(
            rule=self.path,
            view_func=self.controller,
            methods=self.methods)
