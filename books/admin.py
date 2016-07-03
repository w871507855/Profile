from django.contrib import admin

from .models import BookList


class BookListAdmin(admin.ModelAdmin):
    fields = ['cover', 'title', 'author', 'publisher', 'review']
    # list_display = ('title', 'author', 'publisher')

admin.site.register(BookList)


