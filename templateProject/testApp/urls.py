from testApp import views
from django.urls import path


urlpatterns = [
    path('wish/', views.tempview),
]
