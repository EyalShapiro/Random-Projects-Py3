from django.urls import path

from . import views as views


# Define routes as a list of objects
MY_ROUTES = [
    {"path": "", "view": views.home, "name": "home"},
    {"path": "get-listen-qsts/", "view": views.get_listen_qsts, "name": "get_questions"},
    {"path": "get-sent-build-qsts/", "view": views.get_sent_build_qsts, "name": "get_sent_build_questions"},
    {"path": "get-unseen-qsts/", "view": views.get_unseen_qsts, "name": "get_unseen_qsts"},
    {"path": "test_version/", "view": views.test_version, "name": "test_version"},
]


#  Dynamically configure urlpatterns using the routes list


def generate_urlpatterns(routes):
    """Generate URL patterns from a list of route definitions."""
    list_of_keys = ["path", "view", "name"]  # Required keys for validation
    return [
        path(route["path"], route["view"], name=route["name"])
        for route in routes
        if all(key in route for key in list_of_keys)  # Ensure each route has the required keys
    ]


urlpatterns = generate_urlpatterns(MY_ROUTES)
