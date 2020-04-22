from django.db import models


class BookNum(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=36, blank=False,
                             unique=True, default='hi')
    description = models.TextField(max_length=226, blank=True)
    is_open = models.BooleanField(default=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    published = models.DateField(blank=True, null=True)
    number = models.OneToOneField(
        BookNum, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    book = models.ManyToManyField(
        Book,  related_name='author')


class Characters(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(
        Book, related_name='characters', on_delete=models.CASCADE)
