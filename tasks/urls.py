from django.urls import path
from . import views

urlpatterns = [
    # Landing Page
    path('', views.LandingPageView.as_view(), name='index'),

    # Projects
    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('proyectos/crear/', views.ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyectos/editar/<int:pk>/', views.ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/eliminar/<int:pk>/', views.ProyectoDeleteView.as_view(), name='proyecto_delete'),

    # Tasks
    path('tareas/', views.TaskListView.as_view(), name='task_list'),
    path('tareas/crear/', views.TaskCreateView.as_view(), name='task_create'),
    path('tareas/editar/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tareas/eliminar/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
]
