from socket import fromshare
from django import forms
from bookapp.models import BookList
class BookForm(forms.Form):
    book_name=forms.CharField(label='Book name',required=True)
    author=forms.CharField(label='Author name',required=True)
    price=forms.CharField(label='Price',required=True)

class BookModelForm(forms.ModelForm):
    class Meta:
        model=BookList
        fields=['book_name','author','price']

