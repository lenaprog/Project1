from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"), 
    path("search", views.search, name="search"),
    path("newentry", views.new_entry, name="newentry"),
    path("edit", views.edit_entry, name="edit")
]