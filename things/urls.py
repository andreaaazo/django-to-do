from django.urls import path
from .views import HomePageView, add_thing, complete_thing, delete_completed_things

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("add", add_thing, name="add_thing"),
    path("completed/<thing_id>", complete_thing, name="complete_thing"),
    path(
        "delete_completed_things",
        delete_completed_things,
        name="delete_completed_things",
    ),
]
