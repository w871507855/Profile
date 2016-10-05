from django.db import models


class BookList(models.Model):
    cover = models.ImageField(upload_to='cover/%Y/%m/%d')
    # cover = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return self.title


