<h1 align="center">📚 Academic Platform API</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Django-4.2.x-green?style=for-the-badge&logo=django">
  <img src="https://img.shields.io/badge/DRF-3.14.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/PostgreSQL-17-blue?style=for-the-badge&logo=postgresql">
  <img src="https://img.shields.io/badge/Swagger-UI-yellowgreen?style=for-the-badge&logo=swagger">
  <img src="https://img.shields.io/badge/Redoc-ready-orange?style=for-the-badge">
</p>

<p align="center">
  <strong>API RESTful para la gestión académica, diseñada con Django y Django REST Framework, lista para microservicios.</strong>
</p>

<hr/>

## Tabla de Contenidos

- [Tabla de Contenidos](#tabla-de-contenidos)
- [Descripción](#descripción)
- [Requerimientos](#requerimientos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Configuración de la Base de Datos (PostgreSQL 17)](#configuración-de-la-base-de-datos-postgresql-17)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Versionamiento](#versionamiento)
- [Documentación de la API](#documentación-de-la-api)
- [Principales Endpoints](#principales-endpoints)
- [Cambios y Ajustes en la Base de Datos](#cambios-y-ajustes-en-la-base-de-datos)
  - [1. Migraciones iniciales de Django](#1-migraciones-iniciales-de-django)
  - [2. Conflicto con tablas de Django ya existentes](#2-conflicto-con-tablas-de-django-ya-existentes)
  - [3. Conflicto con tablas `user` personalizadas](#3-conflicto-con-tablas-user-personalizadas)
  - [4. Token Blacklist de Django](#4-token-blacklist-de-django)
  - [5. Ajustes en `course_teachers` (autoincrement)](#5-ajustes-en-course_teachers-autoincrement)
  - [6. Ajustes en `course_students` (autoincrement)](#6-ajustes-en-course_students-autoincrement)
- [Licencia](#licencia)

---

## Descripción

Este proyecto implementa una API RESTful para la gestión de una plataforma académica. Permite administrar cursos, semestres, estudiantes, profesores y sus relaciones. Incluye documentación interactiva con Swagger y Redoc, y está preparado para una arquitectura basada en microservicios.

---

## Requerimientos

- **Python** >= 3.12
- **Django** >= 4.2,<5.0
- **Django REST Framework** >= 3.14,<4.0
- **drf-yasg** >= 1.21,<2.0 (Swagger)
- **psycopg2-binary** >= 2.9,<3.0 (driver PostgreSQL)
- **PostgreSQL** 17
- **pip** >= 23.0
- **Virtualenv** (opcional pero recomendado)

**Dependencias completas (`requirements.txt`):**
```
asgiref==3.8.1
attrs==25.3.0
certifi==2025.7.14
cffi==1.17.1
charset-normalizer==3.4.2
colorama==0.4.6
cors==1.0.1
Django==5.2
django-cors-headers==4.7.0
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
drf-spectacular==0.28.0
drf-yasg==1.21.10
filelock==3.18.0
future==1.0.0
gevent==25.5.1
greenlet==3.2.3
idna==3.10
inflection==0.5.1
jsonschema==4.25.1
jsonschema-specifications==2025.9.1
packaging==24.2
psycopg2-binary==2.9.10
pycparser==2.22
PyJWT==2.9.0
PySocks==1.7.1
pytz==2025.2
PyYAML==6.0.2
referencing==0.36.2
requests==2.32.4
requests-file==2.1.0
rpds-py==0.27.1
setuptools==80.9.0
six==1.17.0
sqlparse==0.5.3
tldextract==5.3.0
tzdata==2025.2
uritemplate==4.1.1
urllib3==2.5.0
zope.event==5.1
zope.interface==7.2

```
---

## Instalación y Configuración

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/SantiagoJaraHernandez/Sit_Backend.git
   cd Sit_Backend
   ```

2. **Crea y activa un entorno virtual**

   ```bash
   python -m venv env
   # En Windows:
   env\Scripts\activate
   # En Linux/Mac:
   source env/bin/activate
   ```

3. **Instala las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**  
   Asegúrate de tener PostgreSQL 17 instalado y crea una base de datos y usuario para el proyecto.

5. **Configura el archivo `settings.py`**  
   Modifica la sección `DATABASES` en `microservices_project/settings.py` como se indica abajo.

6. **Aplica las migraciones**

   ```bash
   python manage.py migrate
   ```

7. **Ejecuta el servidor de desarrollo**

   ```bash
   python manage.py runserver
   ```

---

## Configuración de la Base de Datos (PostgreSQL 17)

Asegúrate de tener PostgreSQL 17 instalado y funcionando.  
En tu archivo `microservices_project/settings.py`, configura la conexión así:

```python

# ...existing code...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_bd',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# ...existing code...
```

> **Nota:** Cambia los valores de NAME, USER y PASSWORD según tu configuración local.

---

## Estructura del Proyecto

```
SIT_EndpointsAvances/
│
├── academics/                  # App principal: modelos, vistas y lógica académica
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
├── users/                      # App para gestión de usuarios y autenticación
│   ├── admin.py
│   ├── apps.py
│   ├── managers.py
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── tests.py
│   ├── tokens.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       ├── 0001_initial.py
│       └── 0002_alter_user_options.py
│   └── templates/
│       └── activation_email.html
│
├── microservices_project/      # Configuración global del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py                   # Script principal de Django
├── requirements.txt            # Dependencias del proyecto
└── readme.md                   # Este archivo
```

---

## Versionamiento

Este proyecto sigue el esquema de versionamiento **SemVer** ([Semantic Versioning](https://semver.org/lang/es/)):

- **MAJOR**: Cambios incompatibles en la API.
- **MINOR**: Nuevas funcionalidades compatibles.
- **PATCH**: Corrección de errores y mejoras menores.

Ejemplo de versión: `v1.2.0`

Para ver la versión actual, revisa el archivo `requirements.txt` y los tags del repositorio.

---

## Documentación de la API

Una vez el servidor esté en ejecución, accede a la documentación interactiva:

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Redoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- **Esquema OpenAPI 3:** [`docs/openapi.json`](docs/openapi.json) (generado con drf-spectacular)

### Documentación técnica (carpeta `docs/`)

| Archivo | Descripción |
| ------- | ----------- |
| [`docs/Documentacion_Tecnica_SIT_Backend.docx`](docs/Documentacion_Tecnica_SIT_Backend.docx) | Documentación técnica del proyecto (resumen, descripción, instalación, uso, metodología, resultados y conclusiones). |
| [`docs/manual-tecnico.docx`](docs/manual-tecnico.docx) / [`.pdf`](docs/manual-tecnico.pdf) | Manual técnico: arquitectura, instalación, modelo de datos, autenticación, endpoints y errores. |
| [`docs/openapi.json`](docs/openapi.json) | Especificación OpenAPI 3 de la API. |
| [`docs/index.html`](docs/index.html) | Documentación ReDoc autocontenida (se abre directo en el navegador). |

Para regenerar la especificación: `python manage.py spectacular --file docs/openapi.json --format openapi-json`

---

## Principales Endpoints

| Recurso                | Endpoint Base                | Descripción                        |
|------------------------|-----------------------------|------------------------------------|
| Cursos                 | `/api/courses/`             | CRUD de cursos                     |
| Semestres              | `/api/semesters/`           | CRUD de semestres                  |
| Estudiantes            | `/api/students/`            | CRUD de estudiantes                |
| Profesores             | `/api/teachers/`            | CRUD de profesores                 |
| Cursos por Semestre    | `/api/course-semesters/`    | Relación curso-semestre            |
| Usuarios               | `/api/users/`               | Gestión de usuarios y autenticación |

> **Nota:** Todos los endpoints principales están agrupados y documentados por tags en Swagger/Redoc.

---

## Cambios y Ajustes en la Base de Datos

Para garantizar la correcta integración del proyecto Django con la base de datos PostgreSQL asignada, es necesario realizar algunos cambios y limpiezas previas.  
**Sigue estos pasos solo si tienes conflictos con migraciones o tablas existentes.**

### 1. Migraciones iniciales de Django

Si la tabla `django_migrations` no tiene columna `id`:

```sql
DROP TABLE django_migrations;
```
Luego ejecuta:
```bash
python manage.py migrate
```

---

### 2. Conflicto con tablas de Django ya existentes

Si existen tablas como `django_content_type` y relacionadas:

```sql
DROP TABLE IF EXISTS django_content_type CASCADE;
DROP TABLE IF EXISTS auth_permission CASCADE;
DROP TABLE IF EXISTS auth_group CASCADE;
DROP TABLE IF EXISTS auth_group_permissions CASCADE;
DROP TABLE IF EXISTS auth_user CASCADE;
DROP TABLE IF EXISTS auth_user_groups CASCADE;
DROP TABLE IF EXISTS auth_user_user_permissions CASCADE;
DROP TABLE IF EXISTS django_session CASCADE;
DROP TABLE IF EXISTS django_admin_log CASCADE;
DROP TABLE IF EXISTS django_migrations CASCADE;
```
Luego:
```bash
python manage.py migrate
```

---

### 3. Conflicto con tablas `user` personalizadas

Si existen tablas relacionadas con usuarios personalizados:

```sql
DROP TABLE IF EXISTS user_groups CASCADE;
DROP TABLE IF EXISTS user_user_permissions CASCADE;
DROP TABLE IF EXISTS "user" CASCADE;
```
Luego:
```bash
python manage.py migrate
```

---

### 4. Token Blacklist de Django

Si existen tablas de token blacklist:

```sql
DROP TABLE IF EXISTS token_blacklist_blacklistedtoken CASCADE;
DROP TABLE IF EXISTS token_blacklist_outstandingtoken CASCADE;
```
Luego:
```bash
python manage.py migrate
```

---

### 5. Ajustes en `course_teachers` (autoincrement)

**Problema detectado:**  
Al insertar registros vía Django, la columna `course_teacher_id` quedaba en `NULL` y la base de datos rechazaba la inserción porque la clave primaria no tenía valor por defecto/autoincrement.

**Acción aplicada:**  
Crear la secuencia si no existe, asignarla como `DEFAULT` de la columna y vincularla correctamente:

```sql
-- Crear secuencia si no existe
CREATE SEQUENCE IF NOT EXISTS course_teachers_course_teacher_id_seq;

-- Asignar secuencia como default
ALTER TABLE course_teachers
ALTER COLUMN course_teacher_id
SET DEFAULT nextval('course_teachers_course_teacher_id_seq');

-- Vincular la secuencia a la columna
ALTER SEQUENCE course_teachers_course_teacher_id_seq
OWNED BY course_teachers.course_teacher_id;

-- Ajustar la secuencia al valor máximo actual de la tabla
SELECT setval(
  'course_teachers_course_teacher_id_seq',
  COALESCE((SELECT MAX(course_teacher_id) FROM course_teachers), 1),
  true
);
```

> **IMPORTANTE:** No se modificaron restricciones `CHECK` del campo `status` en esta tabla. Solo se realizó la configuración de la secuencia/autoincremento.

---

### 6. Ajustes en `course_students` (autoincrement)

**Problema detectado:**  
Al insertar registros vía Django, la columna `course_student_id` quedaba en `NULL` y la base de datos rechazaba la inserción porque la clave primaria no tenía valor por defecto/autoincrement.

**Acción aplicada:**  
Crear la secuencia si no existe, asignarla como `DEFAULT` de la columna y vincularla correctamente:

```sql
-- Crear secuencia si no existe
CREATE SEQUENCE IF NOT EXISTS course_students_course_student_id_seq;

-- Asignar secuencia como default
ALTER TABLE course_students
ALTER COLUMN course_student_id
SET DEFAULT nextval('course_students_course_student_id_seq');

-- Vincular la secuencia a la columna
ALTER SEQUENCE course_students_course_student_id_seq
OWNED BY course_students.course_student_id;

-- Ajustar la secuencia al valor máximo actual de la tabla
SELECT setval(
  'course_students_course_student_id_seq',
  COALESCE((SELECT MAX(course_student_id) FROM course_students), 1),
  true
);
```

> **IMPORTANTE:** Tampoco se modificaron restricciones `CHECK` del campo `status` en `course_students`. Los valores válidos siguen siendo los definidos en la BD.

---

> **Recomendación:**  
> Siempre realiza un **backup** de la base antes de aplicar estos cambios.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
