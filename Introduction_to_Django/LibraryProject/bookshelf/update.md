### Update Operation

**Python Command:**

```python
from bookshelf.models import Book

# Assuming the book to update has ID 1 (from the create step).
# In a real shell session, you would use the actual ID of the book you want to modify.
book_to_update = Book.objects.get(id=1)

# Update the title attribute of the retrieved book
book_to_update.title = "Nineteen Eighty-Four"

# Save the changes to the database
book_to_update.save()

# Retrieve the book again to confirm the update
updated_book = Book.objects.get(id=1)
print(f"Updated Title: {updated_book.title}")
