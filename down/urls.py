from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
 #landing page
    path('',views.home , name = 'home'),

    #ergistration urls
    path("register/", views.register_request, name = "register"),
    path("login/", views.login_request, name = "login"),

    #posting urls
    path('add_post/', views.add_post, name="post_details")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
