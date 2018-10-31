from django.urls import path
from poke import views

urlpatterns = [
    path('', views.poke_view, name='poke_view'),
]
