from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('generate', views.generate),
    path('reset', views.reset),
    path('random_word_route', views.random_word_route)
]
