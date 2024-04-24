from django.urls import path
from . import views

app_name = 'board'


urlpatterns = [
    path('', views.BoardList.as_view(), name='list'),
    path('create/', views.BoardCreate.as_view(), name='create'),
    path('<int:pk>/detail/', views.BoardDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BoardUpdate.as_view(), name='edit'),
    path('<int:pk>/remove/', views.BoardDelete.as_view(), name='remove'),
    
    path('search/', views.BoardSearch.as_view(), name='search'),
]

