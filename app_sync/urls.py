from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_sync, name="view-sync"),
]