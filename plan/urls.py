from django.urls import path
from . import views

urlpatterns = [
				path('', views.default, name='default'),
				path('<project_name>/', views.template, name='template'),
				]