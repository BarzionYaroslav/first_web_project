from django.shortcuts import render
from .models import Book

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
                "title": "Services",
                "description": "Check the services this website provides",
                "button": "Visit",
                "image_source": "https://placehold.co/300",
                "href": "pages:index"
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