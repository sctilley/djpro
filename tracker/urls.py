from django.urls import path
from . import views

urlpatters = [
	path('/tracker/', views.tracker, name='tracker')
]