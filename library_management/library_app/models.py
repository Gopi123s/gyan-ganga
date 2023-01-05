from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=150)

    def __str__(self):
        return self.book_name

class Author(models.Model):
    Book=models.ForeignKey(Book,on_delete=models.CASCADE)
    author_name=models.CharField(max_length=150)

    def __str__(self):
        return self.author_name



class Student(models.Model):
    book_name=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    author_name=models.ForeignKey(Author,on_delete=models.CASCADE)
    stu_name=models.CharField(max_length=150,null=False)
    father_name=models.CharField(max_length=150,null=False)
    address=models.CharField(max_length=150,null=False)
    phone=models.IntegerField(default=0)
    issue_date=models.DateField()

    def __str__(self):
        return "%s %s "% (self.stu_name ,self.phone)

