from django.db import models



class Person(models.Model):
    username = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    note = models.TextField(max_length=30, default="your name's" , blank=True, null=True)



class Book(models.Model):
    book_name = models.CharField(max_length=300, blank=False)
    author = models.CharField(max_length=70, blank=True)
    stock_info = models.PositiveIntegerField()
    add_date = models.DateField()