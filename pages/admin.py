from django.contrib import admin

# Register your models here.

from pages.models import Book, Tag

admin.site.register(Book)
admin.site.register(Tag)