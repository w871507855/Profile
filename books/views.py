import pdb
import os

from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import BookList
from .forms import BookListForm


class BookRecommend(generic.ListView):
    model = BookList
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 1


def add_book(request):
    if request.method == 'POST':
        form = BookListForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return HttpResponseRedirect(reverse('books:detail_book', kwargs={'id': book.id}))
    else:
        form = BookListForm()
    return render(request, 'books/add_book.html', {'form': form})


def delete_book(request, id):
    book = get_object_or_404(BookList, id=id)
    messages.add_message(request, messages.WARNING,
                         'The book %s is deleted.' % book.title.upper())
    # delete the file first
    try:
        os.remove(book.cover.path)
    except FileNotFoundError:
        print("File Not Exits!")
    book.delete()
    return HttpResponseRedirect(reverse('books:books'))


def change_book(request, id):
    book = get_object_or_404(BookList, id=id)

    if request.method == 'POST':
        form = BookListForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            # add a message
            messages.add_message(request, messages.INFO, 'Congratulation! Book have been updated.')
            return HttpResponseRedirect(reverse('books:detail_book', kwargs={'id': id}))
    else:
        form = BookListForm(instance=book)
    return render(request, 'books/change_book.html', {'form': form})


def detail_book(request, id=1):
    book = get_object_or_404(BookList, id=id)
    return render(request, 'books/detail_book.html', {'book': book})
