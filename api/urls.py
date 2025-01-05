# api/urls.py
from django.urls import path
from .views import BookList, HelloWorld

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('hello/', HelloWorld.as_view(), name='hello-world'),
]
