from django.urls import path

import pages.views as view

app_name = "pages"

urlpatterns = [
    path("", view.index, name="index"),
    path("categories/", view.categories, name="categories"),
    path("books/", view.book_list, name="books"),
    path("book/<int:id>/", view.book_details, name="book_detail"),
    path("book/<int:id>/edit", view.edit_book, name="edit_book"),
    path("contact/", view.contact, name="contact"),
    path("book/create/", view.create_book, name="create_book")
]