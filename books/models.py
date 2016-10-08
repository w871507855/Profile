from django.db import models
from django.core.urlresolvers import reverse


class BookList(models.Model):
    cover = models.ImageField(upload_to='cover/%Y/%m/%d')
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:detail_book', kwargs={'id': self.id})
