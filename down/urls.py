from django.urls import path
# from views import *
from . import views


urlpatterns = [
 #landing page
    path('',views.home , name = 'home'),

    #ergistration urls
    path("register/", views.register_request, name = "register"),
]
