from . import views
from django.urls import path

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]