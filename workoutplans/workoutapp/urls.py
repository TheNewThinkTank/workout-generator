from django.urls import path
from . import views

urlpatterns = [
    path("welcome_view/", views.welcome_view)
]