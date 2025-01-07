from django.urls import path
from . import views
urlpatterns = [
    path("", views.create_model, name = "create_model")
]