from django.views import generic

from .models import BookList


class BookRecommend(generic.ListView):
    model = BookList
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 1






