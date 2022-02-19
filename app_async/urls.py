from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_async, name="view-async"),
]