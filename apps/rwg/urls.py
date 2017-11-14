from django.conf.urls import url
from . import views #this line is new! #imports views.py from current folder
urlpatterns=[
    url(r'^$', views.index),#this line has changed!,
    url(r'^random_word$',views.random_word),
    url(r'^random_word/reset$',views.reset),
]