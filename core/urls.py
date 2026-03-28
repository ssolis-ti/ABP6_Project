from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')), # Registro de usuarios
    path('', include('tasks.urls')),
]

handler404 = 'django.views.defaults.page_not_found'
