from django.urls import path

import pages.views as view

app_name = "pages"

urlpatterns = [
    path("", view.index, name="index"),
    path("accounts/register", view.register, name="register"),
    path("categories/", view.categories, name="categories"),
    path("books/", view.BookList.as_view(), name="books"),
    path("book/<int:id>/", view.BookDetail.as_view(), name="book_detail"),
    path("book/<int:id>/comment", view.create_comment, name="add_comment"),
    path("book/<int:id>/edit", view.EditBook.as_view(), name="edit_book"),
    path("book/<int:id>/delete",view.DeleteBook.as_view(),name="delete_book"),
    path("contact/", view.contact, name="contact"),
    path("book/create/", view.CreateBook.as_view(), name="create_book")
]