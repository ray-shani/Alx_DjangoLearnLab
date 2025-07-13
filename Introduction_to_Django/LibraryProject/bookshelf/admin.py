from django.contrib import admin
from .models import Book

    # Define a custom ModelAdmin class for the Book model
class BookAdmin(admin.ModelAdmin):
        # 1. Customize list display:
        # This list specifies which fields will be displayed as columns
        # in the change list page of the admin interface.
        list_display = ('title', 'author', 'publication_year', 'id') # Added 'id' for easy reference

        # 2. Configure list filters:
        # This list enables filters on the right sidebar of the admin change list page.
        # Users can click on these filters to narrow down the displayed books.
        list_filter = ('publication_year', 'author')

        # 3. Configure search capabilities:
        # This tuple specifies which fields will be searched when a user
        # types into the search box on the admin change list page.
        # Use '__icontains' for case-insensitive partial matches.
        search_fields = ('title__icontains', 'author__icontains')

        # Optional: Add fields to make clickable links to the detail page
        list_display_links = ('title',)

        # Optional: Add fields that are editable directly from the list view
        # list_editable = ('publication_year',) # Be careful with this in production

    # Unregister the simple registration if it was there, and register with the custom class
    # admin.site.unregister(Book) # Only if you had admin.site.register(Book) previously
admin.site.register(Book, BookAdmin)
    