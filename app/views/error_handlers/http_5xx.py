from werkzeug.exceptions import HTTPException, InternalServerError

from app.base_routes import ErrorView

ERROR_DESCRIPTIONS = {
    500: "The server encountered an unexpected error ._.",
    501: "Woah! You seem to have found something we haven't even implemented yet!",
    502: "This is weird, one of our upstream servers seems to have experienced an error.",
    503: "Looks like one of our services is down for maintenance and couldn't respond to your request.",
    504: "Looks like an upstream server experienced a timeout while we tried to talk to it!",
    505: "You're using an old HTTP version. It might be time to upgrade your browser.",
}


class Error500View(ErrorView):
    name = "errors-5xx"
    error_code = range(500, 600)

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

        # We were sometimes recieving errors from RethinkDB, which were not originating from Werkzeug.
        # To fix this, this section checks whether they have a code (which werkzeug adds) and if not
        # change the error to a Werkzeug InternalServerError.

        if not hasattr(error, "code"):
            error = InternalServerError()

        error_desc = ERROR_DESCRIPTIONS.get(error.code, "We're not really sure what happened there, please try again.")

        return error_desc
