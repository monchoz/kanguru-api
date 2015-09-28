from django.conf.urls import patterns, include, url
from api import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^users/$', views.UserList.as_view()),
)
