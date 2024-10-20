# API views handle the logic for the various API endpoints.

# from django.shortcuts import render
# Create your views here.

from rest_framework import viewsets
from .models import Book, LibraryUser, Transaction
from .serializers import BookSerializer, LibraryUserSerializer, TransactionSerializer
# To Enable Authentication for Library Users
from rest_framework.permissions import IsAuthenticated


# ViewSet for Book model, allowing CRUD operations for books
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to convert data to/from JSON


# ---------------------------------------------------------------------------------------------
# ViewSet for LibraryUser model, allowing CRUD operations for library users
#class LibraryUserViewSet(viewsets.ModelViewSet):
#    queryset = LibraryUser.objects.all()  # Retrieve all library users
#    serializer_class = LibraryUserSerializer  # Use the LibraryUserSerializer for data handling
# ---------------------------------------------------------------------------------------------

# ViewSet for LibraryUser model, allowing only authenticated users to view their own data
class LibraryUserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()  # Retrieve all library users
    serializer_class = LibraryUserSerializer  # Use the LibraryUserSerializer for data handling
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view

    # Override the default queryset to filter by the logged-in user
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Return only the data of the authenticated user
            return LibraryUser.objects.filter(user=self.request.user)
        return LibraryUser.objects.none()  # Return an empty queryset if the user is not authenticated


# ViewSet for Transaction model, allowing CRUD operations for book transactions
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()  # Retrieve all transactions
    serializer_class = TransactionSerializer  # Use the TransactionSerializer for data handling
