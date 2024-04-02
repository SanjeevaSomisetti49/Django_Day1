from django.urls import path
from app.views import *
app_name='app'
urlpatterns = [
    path('Sample/',Sample,name='Sample')
]