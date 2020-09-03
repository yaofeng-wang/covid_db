from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/records/', views.record_list),
    path('api/records/<int:pk>/', views.record_detail),
]