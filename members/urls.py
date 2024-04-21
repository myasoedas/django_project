from django.urls import path
#from . import views
from .views import members

urlpatterns = [
    path('', members, name='hello-world'),
    #path('members/', views.members, name='members'),
    #path('', views.index, name='index'),
]

