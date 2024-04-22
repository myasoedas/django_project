from django.urls import path
from . import views
                
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),  # URL для главной страницы members
    path('members/details/<int:id>/', views.details, name='details'),  # Подробности о члене
]

