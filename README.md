# 🧬 ZETA | ORDEN Y PROGRESO (ABP 6)

Bienvenido al **Gestor de Proyectos Zeta**, una solución robusta y modular desarrollada con Django 6.0.2. Este sistema ha sido diseñado bajo los pilares de **seguridad, escalabilidad y una experiencia de usuario quirúrgica**.

---

<img width="1910" height="916" alt="Zeta Interface" src="https://github.com/user-attachments/assets/7a94f8b2-7cfe-45ad-a0fe-cc97b680f81d" />

## 🛠️ Tecnologías
- **Backend:** Python 3.12+ / Django 6.0+
- **Database:** SQLite3 (Desarrollo) / PostgreSQL (Producción/Docker)
- **Frontend:** Bootstrap 5 (Estética Dark Mode Zeta)
- **Infraestructura:** Docker & Docker Compose

---

## 🚀 Guía de Revisión: Despliegue en Entorno Virtual (Recomendado)

Siga estos pasos simplificados para desplegar la aplicación localmente en menos de 5 minutos:

### 1. Preparación del Entorno
Active el entorno virtual incluido en el proyecto:
- **Windows:** `.\venv\Scripts\activate`
- **Linux/macOS:** `source venv/bin/activate`

### 2. Instalación de Dependencias
Asegúrese de tener instalados los paquetes necesarios:
```bash
pip install -r requirements.txt
```

### 3. Configuración de Base de Datos y Usuarios
Ejecute las migraciones y cree su acceso administrativo:
```bash
python manage.py migrate
python manage.py createsuperuser
```
*(Siga las instrucciones en pantalla para definir su usuario y contraseña)*

### 4. Lanzamiento del Sistema
Inicie el servidor de desarrollo:
```bash
python manage.py runserver
```
Acceda mediante: **http://127.0.0.1:8000/**

---

## 🐳 Despliegue Independiente con Docker

Si prefiere una revisión mediante contenedores orquestados con **PostgreSQL**:

1. Asegúrese de tener Docker Desktop iniciado.
2. En la raíz del proyecto, ejecute:
   ```bash
   docker compose up --build -d
   ```
3. Acceda al sistema en: **http://localhost:8013/**

---

## ⚙️ Características Técnicas (ZETA Standard)

- **Landing Page Premium:** Interfaz de alto impacto con guía de uso integrada.
- **Gestión de Identidad:** Registro de usuarios con validación de Email.
- **Arquitectura Modular:** Separación clara entre `core`, `tasks` (proyectos/tareas) y `users`.
- **Manejo de Errores:** Página 404 personalizada bajo la estética Zeta.
- **Seguridad:** Implementación de `LoginRequiredMixin` y protección CSRF reforzada.

---

## 📂 Organización del Repositorio

- `core/`: Configuración maestra del orquestador Django.
- `tasks/`: Lógica de negocio para proyectos y tareas.
- `users/`: Gestión de cuentas y perfiles.
- `docs/`: Documentación técnica de arquitectura detallada.
- `templates/`: Plantillas HTML con diseño Dark Mode premium.

---

## 🛡️ Notas de Seguridad y Mejores Prácticas

Este repositorio sigue estándares profesionales:
- **.gitignore:** Configurado para excluir `.env`, `db.sqlite3` y entornos virtuales.
- **Clean Code:** Código estructurado y documentado para una revisión técnica fluida.

**MÓDULO 6 | ABP6 PROJECT 2026**
