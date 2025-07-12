# /home/rayshani/Alx_DjangoLearnLab/project_name/book_stores/views.py

from django.shortcuts import render # Or HttpResponse for simple text
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from the Book Stores app (Index Page)!")

def book_list(request):
    # This is the view function that Django is looking for.
    # In a real application, you'd fetch books from a database and render a template.
    return HttpResponse("Hello from the Book Stores app (Book List Page)!")

def book_detail(request, pk): # Assuming you have a book_detail view as well
    return HttpResponse(f"Details for book ID: {pk}")

# Add other view functions as needed for your app