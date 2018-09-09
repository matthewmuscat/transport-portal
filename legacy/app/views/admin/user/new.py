from datetime import datetime
from logging import getLogger

from flask import current_app, redirect, request, url_for

from app.base_routes import RouteView


class UserNewView(RouteView):
    path = "/admin/users/new"
    name = "user/new"
    template = "admin/user/new.html"
    log = getLogger("flask")

    def get(self):
        """
        A page to create a new user
        """

        return self.render(self.template)

    def post(self):
        """
        Create a user and redirect to the DetailView
        :return:
        """

        email = request.form["email"]
        password = request.form["password"]
        group = request.form["group"]
        active = request.form["active"]

        # Convert active to a boolean
        active = True if active == "on" else False

        # Create a user
        datastore = current_app.security.datastore
        datastore.create_user(
            email=email,
            password=password,
            group=group,
            active=active,
            confirmed_at=datetime.now()
        )
        datastore.commit()

        return redirect(url_for("admin.user/list"))
