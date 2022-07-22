from django.urls import path, include
# from views import *
from . import views


urlpatterns = [
    #ergistration urls
    path("register/", views.register_request, name="register"),
 #landing page
    path('',views.home , name='home'),
]
