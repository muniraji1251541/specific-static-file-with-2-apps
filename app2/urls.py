from django.urls import path
from app2.views import *
app_name='any2'

urlpatterns=[
    path('second/',second,name='second'),
]