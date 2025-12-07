from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from management.models import Book , Author , Borrowing
from django.contrib.auth import authenticate, login, logout 
# Create your views here.

def register_views(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists!')
            return redirect('register')

        # Create User
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()

        messages.success(request, 'Account created successfully!')     # Auto login after register
        return redirect('dashboard')  # Go to dashboard

    return render(request, 'register.html')


def login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

        login(request, user)
        return redirect('dashboard')

    return render(request, 'Login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')


def Dashboard(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    users = User.objects.all()
    # print("USERS:", users)
    total_books = Book.objects.count()
    total_members = User.objects.count()
    context = {
        'books': books,
        'authors': authors,
        'users':users,
        'total_books': total_books,
        'total_members': total_members,
    }
    return render(request, 'Dashboard.html', context)
              
def manage_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'managebookes.html', {'books': books})


def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    authors = Author.objects.all()

    if request.method == "POST":
        book.Book_name = request.POST.get('Book_name')
        book.Book_summary = request.POST.get('Book_summary')
        book.Book_price = request.POST.get('Book_price')
        author_id = request.POST.get('author')
        book.author = Author.objects.get(id=author_id) if author_id else None
        book.save()
        return redirect('manage_books')

    return render(request, 'edit_book.html', {'book': book, 'authors': authors})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect('manage_books')

def manage_user(request):
    users = User.objects.all()
    return render(request, 'Manageuser.html', {'users': users})

def edit_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('manage_user')

    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('manage_user')


def ManageAuthorsView(request):
    authors = Author.objects.all()
    return render(request, 'ManageAuthors.html', {'authors': authors})
 
def EditAuthorView(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        author.Author_name = request.POST.get('Author_name')
        author.Author_bio = request.POST.get('Author_bio')
        author.Date_of_birth = request.POST.get('Date_of_birth')
        author.country = request.POST.get('country')
        author.save()
        messages.success(request, "Author updated successfully")
        return redirect('manage_authors')
    return render(request, 'EditAuthor.html', {'author': author})

 
def DeleteAuthorView(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    messages.success(request, "Author deleted successfully")
    return redirect('manage_authors')


def manage_borrowed(request):
    borrowed = Borrowing.objects.select_related('book', 'book__author','user').all()
    return render(request, 'Manageborrowed.html', {'borrowed': borrowed})

def edit_borrowing(request, id):
    borrowing = get_object_or_404(Borrowing, pk=id)
    users = User.objects.all()
    books = Book.objects.all()

    if request.method == "POST":
        user_id = request.POST.get('user')
        book_id = request.POST.get('book')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        returned_at = request.POST.get('returned_at')

        borrowing.user_id = user_id
        borrowing.book_id = book_id
        borrowing.status = status
        borrowing.due_date = due_date
        borrowing.returned_at = returned_at if returned_at else None
        borrowing.save()

        messages.success(request, "Borrowing record updated successfully.")
        return redirect('manage_borrowed')

    return render(request, 'EditBorrowing.html', {
        'borrowing': borrowing,
        'users': users,
        'books': books
    })
    
def deletebrrowingView(request,id):
    borrowed = get_object_or_404(Borrowing, id=id)
    borrowed.delete()
    messages.success(request, "Author deleted successfully")
    return redirect('manage_borrowed')