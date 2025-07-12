# /home/rayshani/Alx_DjangoLearnLab/project_name/book_stores/urls.py

from django.urls import path
from . import views # Assuming you have a views.py in your book_stores app

app_name = 'book_stores' # It's good practice to define an app_name

urlpatterns = [
    # These are URL patterns directly handled by views in the 'book_stores' app
    path('', views.index, name='index'), # e.g., /books/ (if included as /books/)
    path('list/', views.book_list, name='book_list'), # e.g., /books/list/
    path('<int:pk>/', views.book_detail, name='book_detail'), # e.g., /books/1/
    # You should NOT have any `include()` statements here that point back to 'book_stores.urls'
    # or your main project's 'project_name.urls'.
]