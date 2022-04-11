from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/404/PageNotFound", views.notfound, name="notfound"),
    path("wiki/<str:title>", views.title, name="title"),
    path("wiki/new/CreatePage", views.createPage, name="createpage"),
    path("wiki/edit/<str:title>", views.editPage, name="editpage")
]
