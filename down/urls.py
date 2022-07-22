from django.urls import path, include
# from views import *
from . import views


urlpatterns = [
 #landing page
    path('home/',views.home , name='home'),

    #ergistration urls
    path("register/", views.register_request, name="register"),
]
