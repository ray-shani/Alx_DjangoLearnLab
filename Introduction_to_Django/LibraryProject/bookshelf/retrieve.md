### Retrieve Operation

**Python Command:**

```python
from bookshelf.models import Book

# Assuming the book created in `create.md` has ID 1.
# In a real shell session, you would use the actual ID returned from the creation step.
retrieved_book = Book.objects.get(id=1)

# Display all attributes of the retrieved book
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")
print(f"ID: {retrieved_book.id}")

# Expeted output
Title: "1984"
Author: George Orwell
Publication Year: "1949"
ID: 1
