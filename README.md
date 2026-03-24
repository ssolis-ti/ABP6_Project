# ZETA | Gestión de Tareas y Proyectos - ABP 6

Aplicación web desarrollada en Django para la gestión eficiente de tareas y proyectos, desarrollada como evaluación del Módulo 6.

## 🛠️ Tecnologías
- Python 3.12+
- Django 6.0
- SQLite3 (Desarrollo)
- Bootstrap 5 (Frontend)
- Docker & Docker Compose (Opcional para containerización)

## 🚀 Instalación y Uso Local (Entorno Virtual)

1. Clonar el repositorio y navegar a la carpeta raíz:
   ```bash
   cd ABP6_Project
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Realizar migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```

5. Crear superusuario (opcional para acceder a /admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Levantar servidor local:
   ```bash
   python manage.py runserver
   ```
   Acceder en: http://127.0.0.1:8000/

## 🐳 Uso con Docker

Si prefieres ejecutar la aplicación mediante contenedores de forma aislada:

1. Levantar el entorno (asegúrate de estar dentro de `ABP6_Project`):
   ```bash
   docker-compose up --build -d
   ```
2. Acceder en: **http://localhost:8013**

3. Crear Superusuario (para administrar desde /admin):
   ```bash
   docker exec -it abp6-web python manage.py createsuperuser
   ```


## 🧪 Pruebas Unitarias

Para verificar el correcto funcionamiento de los modelos y la seguridad de las rutas, ejecuta la suite de pruebas automatizadas:
```bash
python manage.py test
```

## 🔐 Seguridad y Funcionalidades Principales
- **Protección de rutas:** Todas las URLs (restringidas) utilizan `LoginRequiredMixin`.
- **Aislamiento de datos:** Mediante consultas QuerySet (`get_queryset`), nos aseguramos de que los usuarios únicamente puedan ver y administrar sus propios Proyectos y Tareas.
- **Protección CSRF:** Incluida en cada envío de formulario.
