from django.urls import path
from . import views

urlpatterns = [
				path('', views.default, name='default'),
				path('login/', views.loginPage, name='loginPage'),
				path('updateTodb/', views.taskUpdate, name='taskUpdate'),
				path('<project_name>/', views.template, name='template'),
				path('<project_name>/edit', views.template, name='editTemplate'),
				]