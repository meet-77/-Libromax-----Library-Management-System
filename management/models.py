from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    Author_name = models.CharField(max_length=50)
    Author_bio = models.TextField()
    Date_of_birth = models.DateField()
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Author_name} - {self.country}"

class Book(models.Model):
    Book_name = models.CharField(max_length=50)
    Book_summary = models.TextField()
    Book_price = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.Book_name} - ₹{self.Book_price}"



class Borrowing(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('lost', 'Lost'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowings')

    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    returned_at = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} → {self.book.Book_name} ({self.status})"
