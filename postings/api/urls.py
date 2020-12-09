from .views import BlogPostRudView
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
]
