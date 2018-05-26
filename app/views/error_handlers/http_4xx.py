from werkzeug.exceptions import HTTPException

from app.base_routes import ErrorView
from app.constants import ERROR_DESCRIPTIONS


class Error400View(ErrorView):
    name = "errors.4xx"
    error_code = range(400, 430)

    def __init__(self):
        # Direct errors for all methods at self.return_error
        methods = [
            'get', 'post', 'put',
            'delete', 'patch', 'connect',
            'options', 'trace'
        ]

        for method in methods:
            setattr(self, method, self.error)

    def error(self, error: HTTPException):
        error_desc = ERROR_DESCRIPTIONS.get(error.code, "We're not really sure what happened there, please try again.")

        return error_desc
