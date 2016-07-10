from django.conf.urls import url

from .views import Introduction

app_name = 'formhook'
urlpatterns = [
    # /formhook/
    url(r'^$', Introduction.as_view(), name='create_profile'),
]