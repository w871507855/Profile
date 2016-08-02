from django.conf.urls import url

from .views import Introduction, intro, test, TestViewCover

app_name = 'formhook'
urlpatterns = [
    # /formhook/create/
    url(r'^create/$', Introduction.as_view(), name='create_profile'),
    # /formhook/succed/, if create profile succeded, redirect to this page.
    url(r'^succed/$', intro, name='profile_created'),
    # /formhook/test/: Don't be serious, just for testing.
    url(r'^test/$', test, name='test'),
    # /formhook/testview/: Don't be serious, just for testing.
    url(r'^testview/$', TestViewCover.as_view(), name='view_test'),
]