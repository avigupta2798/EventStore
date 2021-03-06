from django.urls import path
from . import views

app_name = "event"
urlpatterns = [
    path('event/', views.EventView.index, name='home'),
    path('create/', views.add_event, name="createEvent"),
    path('liked/', views.likedEvents, name="likedEvents"),
    path('like/', views.like, name="like")
]