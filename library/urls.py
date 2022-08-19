from django.urls import path
from . import views


urlpatterns={
    path("",views.index,name="index"),
    path("add_book/",views.add_books,name="add_books"),
    path("view_students/",views.view_students,name="view_students"),
    path("issue_book/",views.issue_book,name="issue_book"),
}