from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def all_books(request):
    book_obj = Book.objects.all()
    # books =
    print(book_obj)
    return book_obj




def books_pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(book_obj, 1)
    page = paginator.get_page(page_number)
    context = {
        'books_pagi': page,
        'page': page,
    }
    return render(request, 'books/books_list.html', context)