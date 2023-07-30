from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'