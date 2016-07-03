from django.conf.urls import url

from . import views


app_name = "resume"

urlpatterns = [
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ShowResume.as_view(), name='profile'),
    url(r'^detail/(?P<pk>[0-9]+)/print/$', views.ResumePrint.as_view(), name='print'),
]




