from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = [
    # /books/
    url(r'^$', views.BookRecommend.as_view(), name="Books"),
]
