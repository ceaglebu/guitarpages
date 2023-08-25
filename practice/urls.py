from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exercises', views.exercises, name='exercises'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('record/<int:id>', views.record, name='record'),
    path('exercise/new', views.new_exercise, name='new_exercise'),
    path('exercise/<int:id>', views.exercise, name='exercise'),
]