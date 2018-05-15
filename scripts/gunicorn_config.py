def when_ready(server=None):
    """ server hook that only runs when the gunicorn master process loads """
    print("do database stuff")
