from django.conf.urls import url
from . import views   

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^clear$', views.clear),
    url(r'^result$', views.result),
]