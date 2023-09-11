from django.urls import path

from . import views
from . import components

urlpatterns = [
    path('', views.index, name='index'),
    path('exercises', views.exercises, name='exercises'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('user/<int:id>', views.user, name='user'),
    path('record/<int:id>', views.record, name='record'),
    path('routine/new', views.new_routine, name='new_routine'),
    path('exercise/new', views.new_exercise, name='new_exercise'),
    path('exercise/edit/<int:id>', views.edit_exercise, name='edit_exercise'),
    path('exercise/<int:id>', views.exercise_view, name='exercise'),

    path('components/add_exercise', components.add_exercise, name='component_add_exercise'),
    path('components/new_exercise', components.new_exercise_form, name='component_new_exercise')
]