from django.db import models
#from pygments.lexers import get_lexer_by_name
#from pygments.formatters.heml import HtmlFormatter
#from pygments import highlight


class BookInfo(models.Model):
    name = models.CharField(max_length=50)
    isbn_no = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    author = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Student(models.Model):
    name = models.CharField(max_length=50)
    id_no = models.IntegerField()
    university = models.ForeignKey(University)

    def __str__(self):
        return self.name


