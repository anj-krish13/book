from ast import arg
from email import message
from tkinter.tix import Form
from django import views
from django.shortcuts import redirect, render
from django.views.generic import View
from bookapp.forms import BookForm,BookModelForm
from bookapp.models import BookList, booklist
from django.contrib import messages
# Create your views here.
class BookView(View):
    def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"add_book.html",{"forms":form})
    def post(self,request,*args,**kwargs):
        form=BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added")
            # book_name=form.cleaned_data.get("book_name")
            # author=form.cleaned_data.get("author")
            # price=form.cleaned_data.get("price")
            # print(book_name,author,price)
            # last_list_id=booklist[-1].get('id')
            # id=last_list_id+1
            # form.cleaned_data['id']=id
            # b_name=form.cleaned_data.get("book_name")
            # athr=form.cleaned_data.get("author")
            # price=form.cleaned_data.get("price")
            # booklist.append(form.cleaned_data)
            # BookList.objects.create(book_name=b_name,author=athr,price=price)
            return redirect("all-book")
        else:
            messages.error(request,"error")
            return redirect("all-book")

class BookListView(View):
    def get(self,request,*args,**kwargs):
        # book=booklist
        book=BookList.objects.all()
        return render(request,"book-list.html",{"books":book})


class BookDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        # book=[book for book in booklist if book.get('id')==id]
        book=BookList.objects.filter(id=id)
        return render(request,"book-details.html",{"book":book})

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        BookList.objects.filter(id=id).delete()
        # books=[book for book in booklist if book.get('id')==id].pop()
        # booklist.remove(books)
        messages.success(request,"successfully deleted")
        return redirect("all-book")

class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        # books=[book for book in booklist if book.get('id')==id].pop()
        books=BookList.objects.get(id=id)
        form=BookModelForm(instance=books)
        return render(request,"book-update.html",{"forms":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        fom=BookList.objects.get(id=id)
        form=BookModelForm(request.POST,instance=fom)
        if form.is_valid():
            form.save(form)
            messages.success(request,"updated")
            # book=[book for book in booklist if book.get("id")==id].pop()
            # data=form.cleaned_data
            # book.update(data)
            # BookList.objects.filter(id=id).update(**form.cleaned_data)
            return redirect("all-book")