"""Books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from bookapp.views import BookDeleteView, BookDetailsView, BookListView, BookUpdateView, BookView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/add',BookView.as_view(),name="add-book"),
    path('book/all',BookListView.as_view(),name="all-book"),
    path('book/detail/<int:id>',BookDetailsView.as_view(),name="bookdetails"),
    path('book/change/<int:id>',BookDeleteView.as_view(),name="book-delete"),
    path('book/update/<int:id>',BookUpdateView.as_view(),name="book-update"),
]
