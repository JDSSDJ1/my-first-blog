from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv_page, name = 'cv_page'),
    path('cv/edit/', views.cv_edit, name = 'cv_edit'),
]