"""
URL configuration for library_managemnet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """ 


from django.contrib import admin
from django.urls import path, include
from management.views import Dashboard, register_views , manage_books ,edit_book , delete_book , manage_user,edit_user,delete_user , ManageAuthorsView ,EditAuthorView ,DeleteAuthorView  , manage_borrowed , edit_borrowing , login_views , logout_view
from management.api.views import add_book  , add_author , add_borrowing
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required


schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="Library Management",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', login_required(Dashboard, login_url='/login/') , name='dashboard'),
    path('register/', register_views, name='register'),
    path('login/', login_views, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_book/', add_book, name='add_books'),
    path('manage_books/', manage_books, name='manage_books'),
    path('edit_book/<int:id>/', edit_book, name='edit_book'),
    path('delete_book/<int:id>/', delete_book, name='delete_book'),
    path('manage_user/', manage_user, name='manage_user'),
    path('edit_user/<int:id>/', edit_user, name='edit_user'),
    path('delete_user/<int:id>/', delete_user, name='delete_user'),
    path('add_author/', add_author, name='add_author'), 
    path('manage_authors/', ManageAuthorsView, name='manage_authors'),
    path('edit_author/<int:id>/', EditAuthorView, name='edit_author'),
    path('delete_author/<int:id>/', DeleteAuthorView, name='delete_author'),
    path('add_borrowing/', add_borrowing, name='add_borrowing'), 
    path('manage_borrowed/', manage_borrowed, name='manage_borrowed'),
    path('edit_borrowing/<int:id>/', edit_borrowing, name='edit_borrowing'),
    path('library/', include('management.api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]