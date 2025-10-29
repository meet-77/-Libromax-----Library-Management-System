from django.urls import path
from .views import BookAPIView , BookDetailAPIView, AuthorAPIView ,AuthorDetailAPIView , BorrowindAPIView , BorrowedDetailsAPIView


urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book_detail'), # DRF API
    path('authors/', AuthorAPIView.as_view(), name='Author_list_create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author_detail'),  # GET, PUT, DELETE
    path('borrowing/',BorrowindAPIView.as_view(),name='borrowimg_list_crete'),
    path('borrowing/<int:pk>/', BorrowedDetailsAPIView.as_view(), name='borrowing_detail')
]
