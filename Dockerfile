# Etapa 1: Builder multi-stage
FROM python:3.12-slim-bullseye AS builder

# Configurar variables de entorno vitales para Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema necesarias para compilar paquetes
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Aprovechar caché instalando primero requerimientos
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Etapa 2: Imagen Final (más ligera y segura)
FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar netcat (para entrypoint) y dependencias runtime de libpq
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario y grupo dedicado (no root)
RUN addgroup --system django && adduser --system --group django

# Copiar wheels compiladas del builder e instalarlas
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copiar y transferir todo el código fuente
COPY . .

# Limpiar permisos críticos
RUN mkdir -p /app/staticfiles /app/media && chown -R django:django /app

# Definir usuario final sin privilegios
USER django

# Asegurar script ejecutable (hacerlo en build para evitar fallas)
# RUN chmod +x /app/entrypoint.sh  (En Windows puede necesitarse, lo obviaremos por que user resolverá con git o lo manejamos después)

ENTRYPOINT ["/app/entrypoint.sh"]
