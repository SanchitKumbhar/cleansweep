from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("signup", signup_user, name="signup"),
    path("login", login_user, name="login"),
    path("logout", logoutuser, name="logout"),
    path("authenticate", authenticatepage, name="authenticate"),
    path("client", client, name="client"),
    path("report", reportpage, name="report"),
    path("admin-page", adminpage, name="admin"),
    path("feedback", feedback, name="feedback"),
    path("track", track, name="track"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
