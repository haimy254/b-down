from django.urls import path, include
from . import views


urlpatterns = [
    #ergistration urls
    path("register", views.register_request, name="register")
]
