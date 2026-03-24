from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Proyecto, Tarea

class TareaModeloTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.proyecto = Proyecto.objects.create(nombre='Proyecto Test', descripcion='Test', usuario=self.user)
        self.tarea = Tarea.objects.create(
            titulo='Tarea Test',
            descripcion='Descripción de test',
            estado='pendiente',
            prioridad='media',
            proyecto=self.proyecto,
            creado_por=self.user
        )

    def test_proyecto_creation(self):
        self.assertEqual(self.proyecto.nombre, 'Proyecto Test')
        self.assertEqual(self.proyecto.usuario, self.user)

    def test_tarea_creation(self):
        self.assertEqual(self.tarea.titulo, 'Tarea Test')
        self.assertEqual(self.tarea.proyecto, self.proyecto)
        self.assertEqual(self.tarea.estado, 'pendiente')

class ViewsSeguridadTestCase(TestCase):
    def test_vistas_protegidas(self):
        response = self.client.get(reverse('proyecto_list'))
        self.assertEqual(response.status_code, 302) # Redirige a login
        
        response_task = self.client.get(reverse('task_list'))
        self.assertEqual(response_task.status_code, 302)
