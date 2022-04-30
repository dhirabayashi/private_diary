from . import views
from django.urls import path

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('diary-list/', views.DiaryListView.as_view(), name='diary_list'),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail')
]
