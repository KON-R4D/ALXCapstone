from django.db import models
from django.contrib.auth.models import User


# Define the 'Book' model to store details about books in the library
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    author = models.CharField(max_length=255)  # Author's name
    isbn = models.CharField(max_length=13, unique=True)  # Unique ISBN for each book
    published_date = models.DateField()  # Date when the book was published
    number_of_copies = models.IntegerField()  # Number of copies available in the library

    # Return the book title as the string representation of the model
    def __str__(self):
        return self.title


# Define the 'LibraryUser' model to extend Django's built-in User model
class LibraryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    date_of_membership = models.DateField(auto_now_add=True)  # Automatically set date of membership
    active_status = models.BooleanField(default=True)  # Indicates if the user is active

    # Return the user's username as the string representation of the model
    def __str__(self):
        return self.user.username


# Define the 'Transaction' model to track book checkouts and returns
class Transaction(models.Model):
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)  # The user who checked out the book
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # The book that was checked out
    checkout_date = models.DateTimeField(auto_now_add=True)  # Date and time when the book was checked out
    return_date = models.DateTimeField(null=True, blank=True)  # Date and time when the book was returned

    # Return a string that shows which user checked out which book
    def __str__(self):
        return f"{self.user} checked out {self.book}"
