from django.urls import path
from pages.views import index, about

app_name = "page"

urlpatterns = [
    path("", index, name="root"),
    path("about", about, name="about"),
]
