from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.index, name="main_page"),
    path("<str:room_name>/", views.room, name="room"),
]


urlpatterns += staticfiles_urlpatterns()
