from django.urls import path
from . import views
                
urlpatterns = [
    path('', views.members, name='members'),  # URL для главной страницы members
    path('details/<int:id>/', views.details, name='details'),  # Подробности о члене
]

