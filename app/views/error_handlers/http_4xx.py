from werkzeug.exceptions import HTTPException

from app.base_routes import ErrorView

ERROR_DESCRIPTIONS = {
    400: "You sent us a request that we don't know what to do with.",
    401: "Nope! You'll need to authenticate before we let you do that.",
    403: "No way! You're not allowed to do that.",
    404: "We looked, but we couldn't seem to find that page.",
    405: "That's a real page, but you can't use that method.",
    408: "We waited a really long time, but never got your request.",
    410: "This used to be here, but it's gone now.",
    411: "You forgot to tell us the length of the content.",
    413: "No way! That payload is, like, way too big!",
    415: "The thing you sent has the wrong format.",
    418: "I'm a teapot. Please don't hurt me.",
    429: "Please don't send us that many requests."
}


class Error400View(ErrorView):
    name = "errors-4xx"
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
