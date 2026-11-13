# Tienda Lula

Sistema web desarrollado con Django para facilitar la gestión de productos, categorías, clientes y ventas de una mercería que trabaja por mayor y por menor.

## Funcionalidades

- Registrar, consultar y modificar categorías.
- Registrar y administrar productos.
- Ingresar códigos de barras o generar códigos internos automáticamente.
- Consultar precios y stock disponible.
- Registrar y consultar clientes.
- Registrar ventas asociadas a un cliente.
- Calcular automáticamente el total de cada venta.
- Descontar automáticamente del stock las cantidades vendidas.
- Consultar las ventas realizadas y sus detalles.

## Tecnologías utilizadas

- Python
- Django
- PostgreSQL
- HTML
- CSS
- Git y GitHub

## Requisitos

- Python instalado.
- PostgreSQL instalado y configurado.
- Las dependencias del proyecto indicadas en `requirements.txt`.

## Instalación y ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Consuelo2700/tif_programacion2.git
   ```

2. Ingresar a la carpeta del proyecto:

   ```bash
   cd tif_programacion2
   ```

3. Crear un entorno virtual:

   ```bash
   python -m venv venv
   ```

4. Activar el entorno virtual en Windows:

   ```bash
   venv\Scripts\activate
   ```

5. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

6. Configurar la conexión a PostgreSQL según los datos de la base de datos local.

7. Aplicar las migraciones:

   ```bash
   python manage.py migrate
   ```

8. Iniciar el servidor:

   ```bash
   python manage.py runserver
   ```

9. Abrir en el navegador:

   ```text
   http://127.0.0.1:8000/
   ```

## Proyecto académico

Trabajo Final Integrador de la asignatura Programación II.

Carrera: Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial.

Alumnas: Consuelo Yuhasz y Jessica Duarte.

Docente: Christian Miranda.

Año: 2026.
