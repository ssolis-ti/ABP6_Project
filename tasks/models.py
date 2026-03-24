from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Proyecto")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_inicio = models.DateField(auto_now_add=True, verbose_name="Fecha de Inicio")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proyectos")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]
    PRIORIDADES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=100, verbose_name="Título de la Tarea")
    descripcion = models.TextField(verbose_name="Descripción")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='media')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="tareas")
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tareas_creadas")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.proyecto.nombre})"

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
