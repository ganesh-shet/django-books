from django.shortcuts import render
from django.http import Http404
from .models import Book
from django.db.models import Avg
# Create your views here.

def root(request):
    Books = Book.objects.all().order_by("-ratings")
    num_of_books = Books.count
    avg_ratings = Books.aggregate(Avg("ratings"))  ##ratings__avg
    return render(request, "book_outlet/index.html", {
        "books":Books,
        "total_no_of_books": num_of_books,
        "average_ratings": avg_ratings
    })


def book_details(request, slug):
    try:
        Bookss = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, "book_outlet/book_details.html", {
        "title":Bookss.title,
        "author":Bookss.author,
        "ratings":Bookss.ratings,
        "isBestSeller":Bookss.isBestSeller
    })


