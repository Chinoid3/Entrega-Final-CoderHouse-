# Mi Blog - Proyecto Final Django

## Descripción

Este es un proyecto de blog desarrollado en Django como parte del proyecto final del curso de Python en CoderHouse. La aplicación permite a los usuarios crear, editar y compartir páginas de contenido, así como comunicarse entre sí a través de un sistema de mensajería.

## Características Principales

### Páginas Principales
- **Home**: Página de inicio con información general del blog
- **Acerca de mí**: Página personal del creador del blog
- **Páginas**: Listado de todas las páginas creadas por los usuarios

### Sistema de Usuarios
- **Registro**: Los usuarios pueden crear cuentas con username, email y contraseña
- **Login/Logout**: Sistema de autenticación completo
- **Perfiles**: Cada usuario tiene un perfil con información personal
- **Edición de perfil**: Los usuarios pueden actualizar su información y avatar
- **Cambio de contraseña**: Funcionalidad para cambiar contraseñas

### Gestión de Contenido
- **Crear páginas**: Los usuarios autenticados pueden crear nuevas páginas
- **Editar páginas**: Los autores pueden editar sus propias páginas
- **Eliminar páginas**: Los autores pueden eliminar sus páginas
- **Búsqueda**: Sistema de búsqueda en el contenido de las páginas
- **Editor de texto enriquecido**: Utilizando CKEditor para crear contenido

### Sistema de Mensajería
- **Enviar mensajes**: Los usuarios pueden enviarse mensajes entre sí
- **Bandeja de entrada**: Vista de mensajes recibidos
- **Mensajes enviados**: Historial de mensajes enviados
- **Estado de lectura**: Los mensajes se marcan como leídos automáticamente

## Tecnologías Utilizadas

- **Django 4.2.7**: Framework web principal
- **Python 3.x**: Lenguaje de programación
- **Bootstrap 5**: Framework CSS para el diseño
- **Font Awesome**: Iconografía
- **SQLite**: Base de datos (desarrollo)

## Estructura del Proyecto

```
blog_project/
├── blog_project/          # Configuración principal del proyecto
│   ├── settings.py        # Configuraciones de Django
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # Configuración WSGI
├── pages/                # App principal para páginas del blog
│   ├── models.py         # Modelo Page
│   ├── views.py          # Vistas para CRUD de páginas
│   ├── forms.py          # Formularios para páginas
│   ├── urls.py           # URLs de la app pages
│   └── admin.py          # Configuración del admin
├── accounts/             # App para manejo de usuarios
│   ├── models.py         # Modelo UserProfile
│   ├── views.py          # Vistas de autenticación y perfiles
│   ├── forms.py          # Formularios de usuario
│   ├── urls.py           # URLs de la app accounts
│   └── admin.py          # Configuración del admin
├── messaging/            # App para mensajería
│   ├── models.py         # Modelo Message
│   ├── views.py          # Vistas para mensajería
│   ├── forms.py          # Formularios de mensajes
│   ├── urls.py           # URLs de la app messaging
│   └── admin.py          # Configuración del admin
├── templates/            # Templates HTML
│   ├── base.html         # Template base con navbar
│   ├── pages/            # Templates para páginas
│   ├── accounts/         # Templates para usuarios
│   └── messaging/        # Templates para mensajería
├── static/               # Archivos estáticos
│   ├── css/              # Estilos CSS
│   ├── js/               # JavaScript
│   └── images/           # Imágenes estáticas
├── media/                # Archivos subidos por usuarios
├── manage.py             # Script de administración de Django
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo
```

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd blog_project
   ```

2. **Crear un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   
   **En Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **En macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   - Aplicación web: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

### Pagina (Modelo Principal)
- `title`: Título de la página (CharField)
- `subtitle`: Subtítulo de la página (CharField)
- `content`: Contenido en texto enriquecido (RichTextField)
- `image`: Imagen de la página (ImageField)
- `author`: Autor de la página (ForeignKey a User)
- `created_at`: Fecha de creación (DateTimeField)
- `updated_at`: Fecha de actualización (DateTimeField)

### UserProfile
- `user`: Usuario asociado (OneToOneField a User)
- `first_name`: Nombre (CharField)
- `last_name`: Apellido (CharField)
- `email`: Email (EmailField)
- `avatar`: Avatar del usuario (ImageField)
- `bio`: Biografía (TextField)
- `birth_date`: Fecha de nacimiento (DateField)
- `created_at`: Fecha de creación (DateTimeField)
- `updated_at`: Fecha de actualización (DateTimeField)

### Message
- `sender`: Remitente (ForeignKey a User)
- `receiver`: Destinatario (ForeignKey a User)
- `subject`: Asunto (CharField)
- `content`: Contenido del mensaje (TextField)
- `is_read`: Estado de lectura (BooleanField)
- `created_at`: Fecha de creación (DateTimeField)

## Apartados proximamente en desarrollo
- Message
- UserProfile
