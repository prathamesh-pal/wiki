from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/" , views.search , name="search"),
    path("New/", views.new_page, name="new_page" ),
    path("rendom/", views.rendom, name="rendom"),
    path("edit/<str:title>", views.edit_page, name="edit_page")
]
