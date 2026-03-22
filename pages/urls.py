from django.urls import path

import pages.views as view

app_name = "pages"

urlpatterns = [
    path("", view.index, name="index"),
    path("categories/", view.categories, name="categories"),
]