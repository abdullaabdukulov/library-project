from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm, AuthorForm
from django.contrib.auth.decorators import login_required


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {"books": books})


@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    previous_page = request.GET.get('from', None)
    return render(request, 'books/book_detail.html', {"book": book, 'previous_page': previous_page})


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect('books:book_list')
    form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:add_form')
    form = AuthorForm()
    return render(request, 'books/author_form.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:book_detail', pk=book.pk)
    form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'book': book})


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk, created_by=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('books:book_list')

    return render(request, 'books/confirm_form.html', {'book': book})


@login_required
def my_books(request):
    books = Book.objects.filter(created_by=request.user)
    return render(request, 'books/my_books.html', {'books': books, 'my_book': True})
