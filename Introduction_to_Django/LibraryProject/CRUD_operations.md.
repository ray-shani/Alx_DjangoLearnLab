# 1. Import your model
from library.models import Book
from datetime import date

# 2. Create a Book instance
book1 = Book(title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", publication_date=date(1979, 10, 12))
book1.save()
print(f"Created Book ID: {book1.id}")

# 3. Retrieve the book
retrieved_book = Book.objects.get(id=book1.id)
print(f"Retrieved Book: {retrieved_book.title}")

# 4. Update the title
book_to_update = Book.objects.get(id=book1.id)
book_to_update.title = "The Restaurant at the End of the Universe"
book_to_update.save()
print(f"Updated Book Title: {Book.objects.get(id=book1.id).title}")

# 5. Delete the book instance
book_to_delete = Book.objects.get(id=book1.id)
book_to_delete.delete()
print(f"Book with ID {book1.id} deleted.")

# Optional: Verify deletion
try:
    Book.objects.get(id=book1.id)
except Book.DoesNotExist:
    print("Book confirmed as deleted.")