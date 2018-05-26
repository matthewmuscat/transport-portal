from os import environ

DEBUG_MODE = "FLASK_DEBUG" in environ
PREFERRED_URL_SCHEME = environ.get("PREFERRED_URL_SCHEME", "http")
ERROR_DESCRIPTIONS = {

    # 5XX
    500: "The server encountered an unexpected error ._.",
    501: "Woah! You seem to have found something we haven't even implemented yet!",
    502: "This is weird, one of our upstream servers seems to have experienced an error.",
    503: "Looks like one of our services is down for maintenance and couldn't respond to your request.",
    504: "Looks like an upstream server experienced a timeout while we tried to talk to it!",
    505: "You're using an old HTTP version. It might be time to upgrade your browser.",

    # 4XX
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
