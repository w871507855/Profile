from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = [
    # /books/
    url(r'^$', views.BookRecommend.as_view(), name="books"),
    # /books/add/
    url(r'^add/$', views.add_book, name='add_book'),
    # /books/delete/1/
    url(r'^delete/(?P<id>\d+)/$', views.delete_book, name='delete_book'),
    # /books/change/1/
    url(r'^change/(?P<id>\d+)/$', views.change_book, name='change_book'),
    # /books/detail/1/
    url(r'^detail/(?P<id>\d+)/$', views.detail_book, name='detail_book'),
]
