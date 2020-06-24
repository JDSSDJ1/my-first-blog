from django.urls import path
from cv import views

urlpatterns = [
    path('cv/', views.cv_page),
]