from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.SongList.as_view())
]