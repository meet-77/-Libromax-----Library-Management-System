from django.shortcuts import render, redirect , get_object_or_404 
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from management.models import Book ,Author , Borrowing
from django.contrib import messages 
from django.contrib.auth.models import User
from management.api.serializers import BookSerializer ,Authorserializers , Borrowingserializers
 
def add_book(request):
    authors = Author.objects.all()  # fetch authors for dropdown
    if request.method == 'POST':
        name = request.POST.get('Book_name')
        summary = request.POST.get('Book_summary')
        price = request.POST.get('Book_price')
        author_id = request.POST.get('author')

        if name and summary and price:
            author_instance = Author.objects.get(id=author_id) if author_id else None
            Book.objects.create(
                Book_name=name,
                Book_summary=summary,
                Book_price=int(price),
                author=author_instance
            )
            return redirect('dashboard')

    books = Book.objects.all()
    return render(request, 'Dashboard.html', {'books': books, 'authors': authors})

 
class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailAPIView(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    
    
def add_author(request):
    if request.method == "POST":
        author_name = request.POST.get('Author_name')
        author_bio = request.POST.get('Author_bio')
        date_of_birth = request.POST.get('Date_of_birth')
        country = request.POST.get('country')

        if author_name and author_bio and date_of_birth and country:
            Author.objects.create(
                Author_name=author_name,
                Author_bio=author_bio,
                Date_of_birth=date_of_birth,
                country=country
            )
            messages.success(request, "Author added successfully!")
            return redirect('dashboard')

    authors = Author.objects.all()
    return render(request, 'Dashboard.html', {'author': authors})


# DRF API View (For API Calls)
class AuthorAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = Authorserializers(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Authorserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Author, pk=pk)

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = Authorserializers(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = Authorserializers(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        author = self.get_object(pk)
        serializer = Authorserializers(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return Response({'message': 'Author deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    
    
def add_borrowing(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        book_id = request.POST.get('book')
        due_date = request.POST.get('due_date')
        return_date = request.POST.get('return_date')
        status = request.POST.get('status')

        # ✅ Check required fields
        if user_id and book_id and due_date and status:
            Borrowing.objects.create(
                user_id=user_id,       
                book_id=book_id,      
                due_date=due_date,
                returned_at=return_date,  
                status=status
            )

            messages.success(request, 'Borrowing added successfully ')
            return redirect('dashboard')

        else:
            messages.error(request, 'Please fill all fields ❌')

    # Fetch data to display on the page
    users = User.objects.all()
    books = Book.objects.all()
    borrowed = Borrowing.objects.all()

    return render(request,'Dashboard.html',
        {
            'users': users,
            'books': books,
            'borrowing': borrowed
        }
    )


class BorrowindAPIView(APIView):
    def get(self,request):
        borrowed = Borrowing.objects.all()
        serializer = Borrowingserializers(borrowed,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = Borrowingserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
    
class BorrowedDetailsAPIView(APIView):

    def get(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk)
        serializer = Borrowingserializers(borrowing)
        return Response(serializer.data)

    def put(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk)
        serializer = Borrowingserializers(borrowing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk)
        serializer = Borrowingserializers(borrowing, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk)
        borrowing.delete()
        return Response({'message': 'Borrowing deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    