# URLs map endpoints to their corresponding views.

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


# Create a router and register viewsets for books, users, and transactions
router = DefaultRouter()
router.register(r'books', views.BookViewSet)  # Register the BookViewSet under the 'books/' route
router.register(r'users', views.LibraryUserViewSet)  # Register the LibraryUserViewSet under the 'users/' route
router.register(r'transactions', views.TransactionViewSet)  # Register the TransactionViewSet under the 'transactions/' route

# Define the URL patterns, which include the registered routes
urlpatterns = [
    path('', include(router.urls)),  # Include all routes defined by the router
]
