from django.db import models

# Create your models here.
class Book(models.Model):
        # CharField for the title with a maximum length of 200 characters
        title = models.CharField(max_length=200)
        # CharField for the author with a maximum length of 100 characters
        author = models.CharField(max_length=100)
        # IntegerField for the publication year
        publication_year = models.IntegerField()

        # This method defines how a Book object will be represented as a string.
        # It's very useful when you print a Book object in the shell or admin.
        def __str__(self):
            return f"{self.title} by {self.author} ({self.publication_year})"
    