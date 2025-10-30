from django.contrib import admin
from .models import Book

# Register Book with custom admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # fields to show in list view
    list_filter = ('author', 'publication_year')            # sidebar filters
    search_fields = ('title', 'author')                     # search box
