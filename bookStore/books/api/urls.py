from django.contrib import admin 
from django.urls import path,include
from books.api.views import BookListCreateAPIView,BookDetailAPIView
urlpatterns = [
    path('books',BookListCreateAPIView.as_view(),name="books-list"),
    path('books/<int:pk>',BookDetailAPIView.as_view(),name="books-detail"),
]