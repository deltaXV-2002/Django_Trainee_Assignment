from django.urls import path
from . import views
urlpatterns = [
    path("", views.test_signal, name = "test_signal")
]