from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponse
from .models import Book, Comment
from .forms import FeedbackForm, BookForm, MyUserCreationForm, CommentForm
from django.urls import reverse, reverse_lazy

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

class BookList(ListView):
    model = Book
    template_name = 'pages/books.html'
    context_object_name = 'products'

class BookDetail(DetailView):
    model = Book
    template_name = 'pages/book_detail.html'
    context_object_name = "book"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

def contact(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("pages:index")
    else:
        form = FeedbackForm()
    
    return render(request, 'pages/contact.html', {"form": form})

class CreateBook(LoginRequiredMixin, CreateView):
    form_class = BookForm
    template_name = 'pages/item_form.html'
    success_url = "pages:book_detail"

    def form_valid(self, form: BookForm):
        form.instance.author = self.request.user
        messages.success("Book created successfully")
        return super().form_valid(form)

class EditBook(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'pages/item_form.html'
    success_url = "pages:book_detail"
    pk_url_kwarg = "id"
    def test_func(self):
        return self.request.user == self.get_object().author

class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("pages:books")
    template_name = 'pages/book_confirm_delete.html'
    pk_url_kwarg = "id"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

def register(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect(reverse("login"))
    else:
        form = MyUserCreationForm()
    
    return render(request, 'registration/register.html', {"form": form, "title": "Registering..."})

@login_required
def create_comment(request, id):
    book = get_object_or_404(Book, id=id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment: Comment = form.save(commit=False)
        comment.author = request.user
        comment.book = book
        comment.save()
        messages.success(request, 'Comment was posted!')
    else:
        messages.error(request, "Error while creating comment!")

    return redirect("pages:book_detail", book.id)