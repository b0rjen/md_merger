# **MD Merger**

Una aplicación sencilla en **Streamlit** para concatenar archivos de texto y código en un solo documento Markdown.

## **Descripción**

MD Merger es una herramienta que permite:

- Cargar múltiples archivos con extensiones `.md`, `.txt`, `.py`, `.js` (vendrán más tipos en futuras versiones).
- Combinar el contenido de estos archivos en un solo archivo `Documentación_indexada.md`.
- Precisamente, el ejemplo que se adjunta en este proyecto, junta este archivo readme con el archivo .py de main, para observar el output.
- Agregar separadores y encabezados entre cada archivo para facilitar la navegación.
- Abrir la carpeta de salida directamente desde la aplicación.

## **Características**

- **Interfaz de Usuario Simple**: Construida con Streamlit para facilitar la interacción.
- **Soporte para Varios Tipos de Archivos**: Admite archivos de texto plano y código fuente.
- **Personalización**: Permite seleccionar la ruta de salida y decidir si sobrescribir o agregar al archivo existente.

## **Requisitos**

- Python 3.9 o superior
- [Poetry](https://python-poetry.org/) para la gestión de dependencias

## **Instalación**

. **Clonar el repositorio**:

```bash
git clone https://github.com/b0rjen/md_merger.git
cd md_merger
```

## Instalar dependencias con Poetry:

```bash
poetry install
```

## Uso

Ejecutar la aplicación:

```bash
  poetry run streamlit run main.py
```

Configuración: Especifica la ruta de la carpeta donde se guardará el archivo combinado.

Carga de Archivos: Selecciona los archivos que deseas combinar.

Procesar Archivos: Haz clic en el botón para iniciar el proceso.

Abrir Carpeta: Utiliza el botón para abrir la carpeta de salida directamente.

Dependencias

Las principales dependencias del proyecto son:

Streamlit: Para crear la interfaz de usuario.

Estas dependencias se gestionan automáticamente con Poetry.

## Licencia

Este proyecto está bajo la Licencia MIT.

## Autor

[@b0rjen](https://github.com/b0rjen)
