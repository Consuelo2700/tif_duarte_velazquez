# Tienda Lula – Sistema de gestión

## Descripción del proyecto

Tienda Lula es una aplicación web desarrollada con Python y Django, que permite gestionar las operaciones de una tienda.

El sistema cuenta con diferentes módulos para administrar productos, categorías, clientes y ventas.

## Requisitos previos para ejecutar un proyecto

Antes de ejecutar el proyecto, es necesario tener instalados:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/downloads/)

## Instalación y configuración

### 1. Descargar el proyecto

Clonar el repositorio desde GitHub:

```bash
git clone https://github.com/Consuelo2700/tif_programacion2.git
```

Ingresar a la carpeta del proyecto:

```bash
cd tif_programacion2
```

### 2. Crear un entorno virtual

Crear un entorno virtual para instalar las dependencias del proyecto:

```bash
python -m venv venv
```

Activar el entorno virtual:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

Con el entorno virtual activado, ejecutar:

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

El proyecto utiliza variables de entorno para almacenar la clave secreta de Django y las credenciales de conexión a PostgreSQL.

En la carpeta principal del proyecto (donde se encuentra `manage.py`), crear un archivo llamado `.env` y agregar las siguientes variables:

```env
DJANGO_SECRET_KEY=tu_clave_secreta
DB_NAME=nombre_de_tu_base
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

Reemplazar los valores de ejemplo por los correspondientes a la configuración local.

### 5. Configurar la base de datos

El proyecto utiliza PostgreSQL como sistema de gestión de bases de datos.

Es necesario:

1. Tener PostgreSQL instalado y en funcionamiento.
2. Crear una base de datos para el proyecto.
3. Verificar que las credenciales configuradas en el archivo `.env` correspondan con las de PostgreSQL.

### 6. Ejecutar las migraciones

Con la base de datos creada y configurada, ejecutar:

```bash
python manage.py migrate
```

Este comando creará las tablas necesarias para el funcionamiento de la aplicación.

### 7. Iniciar el servidor

Para ejecutar la aplicación web, utilizar:

```bash
python manage.py runserver
```

Luego, abrir el navegador e ingresar a:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
