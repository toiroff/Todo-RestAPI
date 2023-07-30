from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',BookListView.as_view(),name='index')
]
