from django.urls import path

from . import views

##############

app_name = 'discordbot'
urlpatterns = [
    path('reactions', views.allreactions, name="amongus-tracker-post"),
]
