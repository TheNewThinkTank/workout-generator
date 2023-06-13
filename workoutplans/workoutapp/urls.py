from django.urls import path
from . import views

urlpatterns = [
    path("welcome_view/", views.welcome_view),
    path("nfp_view/", views.nfp_view),
]