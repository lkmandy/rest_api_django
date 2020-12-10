from .views import BlogPostRudView, BlogPostAPIView
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
        url(r'^$', BlogPostAPIView.as_view(), name='post-create'),
        url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
]
