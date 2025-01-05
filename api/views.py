from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello World"}, status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()  # Get all books from the database
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

