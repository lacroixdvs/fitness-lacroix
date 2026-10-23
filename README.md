# Fitness Lacroix - Backend EFI

Backend API REST para la plataforma de planes de entrenamiento Fitness Lacroix.
Proyecto final - Programación II - 3 de Noviembre 2026

**Alumno:** Nico Lacroix

## 🚀 Stack Tecnológico
- **Python 3.12 + Django 5**
- **Django REST Framework**
- **drf-spectacular** (Swagger / OpenAPI)
- **django-filter** (Filtros avanzados)
- **uv** (Gestor de paquetes)
- **Docker + Docker Compose**
- **SQLite**

## ✅ Requisitos EFI Cumplidos

| Requisito | Implementación |
|---|---|
| **CRUD Completo** | `PlanLacroixViewSet` con ModelViewSet |
| **Serializers Anidados** | `Beneficios` como JSONField + validación |
| **Paginación** | PageNumberPagination ordenada por `id` |
| **Filtros** | `list_filter` por `nivel` y `precio`, `search_fields` por `nombre` |
| **Documentación** | Swagger en `/api/schema/swagger/` |
| **Admin Custom** | `list_display`, `list_filter`, `search_fields` |
| **Docker** | `Dockerfile` + `docker-compose.yml` listo para deploy |

## 📦 Instalación Local (sin Docker)

```bash
# Clonar
git clone <tu-repo>
cd fitness-lacroix-backend

# Instalar dependencias
uv sync

# Migraciones
uv run python manage.py migrate

# Crear superuser (admin / admin123)
uv run python manage.py createsuperuser

# Cargar datos de prueba
uv run python manage.py shell