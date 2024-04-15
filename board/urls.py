from django.urls import path
from . import views

app_name = 'board'


urlpatterns = [
    path('', views.BoardList.as_view(), name='list'),
    path('create/', views.BoardCreate.as_view(), name='create'),
    path('<int:pk>/detail/', views.BoardDetail.as_view(), name='detail'),
]
