# Proyecto Django REST - Gestión de Pacientes

Este proyecto es un ejemplo de una API para gestionar pacientes utilizando Django y Django REST Framework.

## Características

- CRUD completo para el manejo de pacientes (crear, listar, actualizar y eliminar).
- Búsqueda de pacientes por diagnóstico a través de una acción personalizada.
- Página HTML inicial que consume la API para mostrar la lista de pacientes con un diseño básico usando Bootstrap.
- Tests automatizados con `APITestCase` de DRF.
- Documentación de la API con OpenAPI/Swagger (opcional con `drf-spectacular` o `drf-yasg`).

## Requerimientos Previos

- Python 3.10 o superior (recomendado)
- pip (para instalar dependencias)

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/tu-repo.git
    cd tu-repo
    ```

2. Crear y activar un entorno virtual (opcional pero recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
   En Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplicar migraciones:
    ```bash
    python manage.py migrate
    ```

5. Iniciar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

   La API estará disponible en `http://localhost:8000/api/patients/` la lista en `http://localhost:8000/lista_pacientes/`. y la documentación en `http://localhost:8000/swagger/`

## Uso

- **Listar Pacientes**: `GET /api/patients/`
- **Crear Paciente**: `POST /api/patients/` (enviar JSON con datos)
- **Actualizar Paciente**: `PUT /api/patients/{id}/`
- **Eliminar Paciente**: `DELETE /api/patients/{id}/`
- **Filtrar por diagnóstico**: `GET /api/patients/por_diagnostico/?q=gripal`

Además, si activaste Swagger/Redoc:

- `GET /swagger/` para la documentación Swagger.
- `GET /redoc/` para la documentación Redoc.

## Tests

Para ejecutar los tests:
```bash
python manage.py test
