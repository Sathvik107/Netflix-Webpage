from django.urls import path
from .index import home
urlpatterns = [
path('',home, name='home')
]
