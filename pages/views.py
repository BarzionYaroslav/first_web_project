from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .forms import FeedbackForm

# Create your views here.
def index(request):
    context = {
        "title": "Main Exchange Page",
        "welcome_text": "Greetings and welcome to BOOK BOOKER",
        "cards": [
            {
                "title": "Products",
                "description": "Scroll through our great assortment of books, now available in all flavors of Touhou Project",
                "button": "Scroll",
                "image_source": "https://placehold.co/300",
                "href": "pages:books"
            },
            {
                "title": "Posts",
                "description": "Check out the posts about your favorite books and general website news",
                "button": "Check out",
                "image_source": "https://placehold.co/300",
                "href": "pages:index"
            },
            {
                "title": "Support",
                "description": "Contact our support team for anything, really!",
                "button": "Contact",
                "image_source": "https://placehold.co/300",
                "href": "pages:contact"
            }
        ]
    }
    return render(request, 'pages/index.html', context)

def categories(request):
    context = {
        "categories": [
            {"title": "Drama", "description": "So Dramatic!"},
            {"title": "Comedy", "description": "So Comedic!"},
            {"title": "Books", "description": "So Books!"},
            {"title": "More books", "description": "So More Books!"},
            {"title": "Not Books", "description": "I can't believe it's Not Books!"}
        ]
    }
    return render(request, 'pages/categories.html', context)

def book_list(request):
    products = Book.objects.all()
    context = {
        "products": products
    }
    return render(request, 'pages/books.html', context)

def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    context = {
        "book": book
    }
    return render(request, 'pages/book_detail.html', context)

def contact(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("pages:index")
    else:
        form = FeedbackForm()
    
    return render(request, 'pages/contact.html', {"form": form})