from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarea, Proyecto
from .forms import TareaForm, ProyectoForm

class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'tasks/proyecto_list.html'
    context_object_name = 'proyectos'
    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'tasks/proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'tasks/proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')
    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'tasks/proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')
    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

class TaskListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tasks/task_list.html'
    context_object_name = 'tareas'
    def get_queryset(self):
        return Tarea.objects.filter(proyecto__usuario=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    def get_queryset(self):
        return Tarea.objects.filter(creado_por=self.request.user)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
    def get_queryset(self):
        return Tarea.objects.filter(creado_por=self.request.user)
