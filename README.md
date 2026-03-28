# 🧬 ZETA | GESTOR DE PROYECTOS (ABP 6)

Bienvenido al **Gestor de Proyectos Zeta**, una solución robusta y modular desarrollada con Django 6.0.2. **.

---

<img width="1910" height="916" alt="Zeta Interface" src="https://github.com/user-attachments/assets/7a94f8b2-7cfe-45ad-a0fe-cc97b680f81d" />

##  Tecnologías
- **Backend:** Python 3.12+ / Django 6.0+
- **Database:** SQLite3 (Desarrollo) / PostgreSQL (Producción/Docker)
- **Frontend:** Bootstrap 5 (Estética Dark Mode Zeta)
- **Infraestructura:** Docker & Docker Compose

---

##  Guía de Revisión: Despliegue Local desde Cero (Recomendado)

Siga este manual paso a paso para levantar la plataforma en su entorno local partiendo desde un estado limpio.

### 1. Variables de Entorno (Requisito Seguridad)
El sistema está protegido criptográficamente y requiere variables para operar.
1. Localice el archivo `env.example` en la raíz del proyecto.
2. Realice una copia exacta de este y renómbrela a **`.env`** (debe incluir el punto inicial).
3. *(Las configuraciones para desarrollo local ya vienen listas por defecto en ese archivo).*

### 2. Creación del Entorno Virtual 
Para mantener las librerías aisladas de su sistema, genere un entorno virtual:
```bash
python -m venv venv
```

### 3. Activación del Entorno
Active el entorno que acaba de crear (según su sistema operativo):
- **Windows:** 
  ```bash
  .\venv\Scripts\activate
  ```
- **Linux / macOS:** 
  ```bash
  source venv/bin/activate
  ```
*(Verificará el éxito si observa el prefijo `(venv)` al inicio de su línea de comandos).*

### 4. Instalación de Dependencias
Asegúrese de instalar la versión exacta del framework y librerías requeridas:
```bash
pip install -r requirements.txt
```

### 5. Generación de Base de Datos
Construya la estructura de tablas inicial ejecutando las migraciones:
```bash
python manage.py migrate
```

### 6. Creación de Usuario Administrador
Para probar la plataforma, genere su propio acceso:
```bash
python manage.py createsuperuser
```
*(Siga las instrucciones en pantalla para definir su usuario, email y contraseña).*

### 7. Lanzamiento del Servidor Django
Inicie el servicio de desarrollo para acceder al frontend:
```bash
python manage.py runserver
```
 **Acceda mediante su navegador a:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

##  Despliegue Independiente con Docker

Si prefiere una revisión mediante contenedores orquestados con **PostgreSQL**:

1. Asegúrese de tener Docker Desktop iniciado.
2. En la raíz del proyecto, ejecute:
   ```bash
   docker compose up --build -d
   ```
3. Acceda al sistema en: **http://localhost:8013/**

---

##  Características Técnicas (ZETA Standard)

- **Landing Page:** Interfaz de alto impacto con guía de uso integrada.
- **Gestión de Identidad:** Registro de usuarios con validación de Email.
- **Arquitectura Modular:** Separación clara entre `core`, `tasks` (proyectos/tareas) y `users`.
- **Manejo de Errores:** Página 404 personalizada bajo la estética Zeta.
- **Seguridad:** Implementación de `LoginRequiredMixin` y protección CSRF reforzada.

---

##  Organización del Repositorio

- `core/`: Configuración maestra del orquestador Django.
- `tasks/`: Lógica de negocio para proyectos y tareas.
- `users/`: Gestión de cuentas y perfiles.
- `docs/`: Documentación técnica de arquitectura detallada.
- `templates/`: Plantillas HTML con diseño Dark Mode premium.

---

**MÓDULO 6 | ABP6 PROJECT 2026**
