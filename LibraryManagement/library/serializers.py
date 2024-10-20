#Serializers are used to convert model instances into JSON and vice versa.

from rest_framework import serializers
from .models import Book, LibraryUser, Transaction


# Serializer for the Book model to handle book data (convert to/from JSON)
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields in the Book model


# Serializer for the LibraryUser model to handle library user data
class LibraryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = '__all__'  # Serialize all fields in the LibraryUser model


# Serializer for the Transaction model to handle book transactions (checkouts and returns)
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'  # Serialize all fields in the Transaction model
