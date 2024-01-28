from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    published_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.book_name
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    owner_of_comment = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True) 
    def __str__(self):
        return self.comment
