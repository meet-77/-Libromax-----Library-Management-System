from rest_framework import serializers
from management.models import Book , Author, Borrowing

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'Book_name', 'Book_summary', 'Book_price']
        
class Authorserializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','Author_name','Author_bio','Date_of_birth','country']

 
class Borrowingserializers(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ['id','user','book' , 'borrowed_at','due_date','returned_at','status']