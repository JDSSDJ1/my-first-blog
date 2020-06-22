from django.urls import path
from . import views

urlpatterns = [
    # path('home', views.post_list, name='post_list'),
    path('home/', views.home_page),
]