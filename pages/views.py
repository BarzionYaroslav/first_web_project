from django.shortcuts import render

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
                "image_source": "https://placehold.co/300"
            },
            {
                "title": "Posts",
                "description": "Check out the posts about your favorite books and general website news",
                "button": "Check out",
                "image_source": "https://placehold.co/300"
            },
            {
                "title": "Services",
                "description": "Check the services this website provides",
                "button": "Visit",
                "image_source": "https://placehold.co/300"
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