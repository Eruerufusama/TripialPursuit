from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.question, name='quiz-question'),
    path('', views.menu, name='quiz-menu'),
    path('about/', views.about, name='quiz-about'),
]
