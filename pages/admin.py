from django.contrib import admin

# Register your models here.

from pages.models import Book

admin.site.register(Book)