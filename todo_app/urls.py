from django.urls import path
from . import views

urlpatterns = [
    #Add Task functionality
    path('addTask/',views.addTask,name='addTask'),

    #  mark_as_done functionality
    path('mark_as_done/<int:pk>/', views.mark_as_done, name="mark_as_done"),
    #  mark_as_done functionality
    path('mark_as_undone/<int:pk>/',views.mark_as_undone, name="mark_as_undone"),

    #  edit tasks functionality
    path('edit_task/<int:pk>/',views.edit_task, name="edit_task"),

    # delete tasks functionality
    path('delete_task/<int:pk>/',views.delete_task, name="delete_task"),
]
