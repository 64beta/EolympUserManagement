from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = "index"),
    path('eliminate/', views.eliminate, name='eliminate'),
    path('about/', views.about, name='about'),
    path('analysis/', views.analysis, name='analysis'),
]
