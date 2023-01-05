from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('avl_book/',avl_book),
    path('issue_book/',issue_book),
    path('issue_book_student/',issue_book_student,name='issue_book_student'),
    # path('issue_book_student/<slug:stu_name>',issue_book_student),
    path('delete/<int:stu_id>',delete),
    # path('issue_book_student/<int:author_id>',issue_book_student),
]
