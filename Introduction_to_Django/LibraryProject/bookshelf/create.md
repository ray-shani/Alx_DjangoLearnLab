
**Python Command:**

```python
from bookshelf.models import Book

# Command to create a Book instance
book_1984 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Print the created book to see its details and confirm creation
print(book_1984)
print(f"Book ID: {book_1984.id}")
```