# 🏛️ Arquitectura y Estructura del Proyecto

Este documento detalla la organización de carpetas y las funcionalidades principales de la plataforma **ZETA | ABP 6**.

## 📂 Estructura de Directorios

La aplicación sigue el patrón estándar de Django, organizada de forma modular para separar las responsabilidades:

```text
ABP6_Project/
├── core/                # Configuración central del proyecto
│   ├── settings.py      # Ajustes de base de datos, seguridad y aplicaciones
│   ├── urls.py          # Enrutamiento global de la plataforma
│   └── wsgi.py/asgi.py  # Interfaces para servidores de despliegue
├── tasks/               # Aplicación de Gestión de Negocio
│   ├── models.py        # Definición de Proyectos y Tareas (ER)
│   ├── views.py         # Lógica CRUD (Create, Read, Update, Delete)
│   ├── forms.py         # Validaciones de formularios de negocio
│   └── templates/       # Vistas HTML específicas para proyectos y tareas
├── users/               # Aplicación de Identidad y Acceso
│   ├── views.py         # Gestión de registro de nuevos usuarios
│   └── urls.py          # Rutas locales de autenticación
├── templates/           # Componentes UI globales (Layout base)
├── static/              # Recursos estáticos (CSS personalizado Zeta, JS)
├── media/               # Directorio para archivos subidos por usuarios
├── docs/                # Documentación técnica y manuales
├── Dockerfile           # Configuración de construcción de imagen Docker
└── docker-compose.yml   # Orquestación de servicios (App + Base de Datos)
```

## ⚙️ Funcionalidades Principales

### 0. Página de Inicio (Landing Page)

- **Vista Pública:** Accesible para todos los usuarios (`LandingPageView`).
- **Propósito:** Presentar las capacidades de la plataforma Zeta y dirigir a los usuarios al registro o inicio de sesión.

### 1. Gestión de Identidad (Auth)

- **Registro:** Los usuarios pueden crear nuevas cuentas (`SignUpView`).
- **Autenticación:** Sistema de Login y Logout integrado con Django Contrib Auth.
- **Seguridad:** Uso de `LoginRequiredMixin` para asegurar que solo usuarios autenticados accedan a la gestión de datos.

### 2. Gestión de Proyectos

- Los usuarios pueden crear **Proyectos** para agrupar sus tareas.
- **Aislamiento:** Cada usuario solo puede ver, editar o eliminar los proyectos que ha creado él mismo.

### 3. Gestión de Tareas

- Las tareas están vinculadas obligatoriamente a un proyecto.
- **Atributos:** Poseen estados (`Pendiente`, `En Progreso`, `Completada`) y niveles de prioridad (`Baja`, `Media`, `Alta`).
- **Filtrado:** La plataforma garantiza que un usuario solo pueda asignar tareas a proyectos de su propiedad.

### 4. Persistencia y Despliegue (Docker)

- **Base de Datos:** PostgreSQL en contenedor independiente para producción/despliegue.
- **Coordinación:** El script `entrypoint.sh` asegura que la aplicación espere a que la base de datos esté lista antes de ejecutar migraciones y levantar el servidor.
- **Entorno:** Configuración dinámica mediante variables de entorno en el archivo `.env`.

## 🛠️ Tecnologías Clave

- **Backend:** Django 6.0.2 & Python 3.12.
- **Frontend:** HTML5, CSS3 Zeta-Design, Bootstrap 5.
- **Infraestructura:** Docker & Docker Compose.
- **Base de Datos:** PostgreSQL (Docker) / SQLite3 (Local opcional).

---

### Documentación generada para el equipo de Desarrollo Web - ABP 6
