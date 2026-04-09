from django.urls import path

import pages.views as view

app_name = "pages"

urlpatterns = [
    path("", view.index, name="index"),
    path("categories/", view.categories, name="categories"),
    path("books/", view.book_list, name="books"),
    path("book/<int:id>/", view.book_details, name="book_detail"),
]