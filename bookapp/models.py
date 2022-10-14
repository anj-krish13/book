from django.db import models

# Create your models here.
booklist=[

    {"id":1,'book_name':"avengers","author":"Russo brothers","price":4900},
    {"id":2,"book_name":"infinity","author":"ravi","price":4500},
    {"id":3,"book_name":"task3","author":"arjun","price":3800},
    {"id":4,"book_name":"task4","author":"aravind","price":4500},
    {"id":5,"book_name":"task5","author":"arjun","price":500},
    {"id":6,"book_name":"task6","author":"hari","price":700},

    
]
class BookList(models.Model):
    book_name=models.CharField(max_length=200)
    author=models.CharField(max_length=150)
    price=models.PositiveIntegerField()
