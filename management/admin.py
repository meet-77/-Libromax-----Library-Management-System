from django.contrib import admin
from .models import Author, Book , Borrowing


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Author_name', 'country', 'Date_of_birth')
    search_fields = ('Author_name', 'country')
    list_filter = ('country',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('Book_name', 'Book_price', 'author')
    search_fields = ('Book_name', 'author__Author_name')
    list_filter = ('author',)


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['user','book' , 'borrowed_at','due_date','returned_at','status']