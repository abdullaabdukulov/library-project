from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('', views.book_list, name="book_list"),
    path('book/<int:pk>', views.book_detail, name="book_detail"),
    path('book/add', views.add_book, name='add_book'),
    path('author/add', views.add_author, name='add_author'),
    path('book/edit/<int:pk>', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>', views.delete_book, name='delete_book'),
    path('my-books/', views.my_books, name='my_books'),
]
