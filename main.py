### Md Merger by b0rjen ### 
### Versión 1.0 ###
### Actualizado para poder hacer uso de la nube de Streamlit además de en local ###
import streamlit as st # Importar la librería Streamlit 
import os # Para manejar rutas de archivos y carpetas
import tempfile  # Para manejar carpetas temporales en la nube
import subprocess # Para ejecutar comandos en la terminal 
import sys # Para obtener la versión de Python instalada

# Título de la aplicación
st.title("Md Merger by b0rjen")

# Descripción de la aplicación
st.subheader("Esta app permite concatenar archivos de texto plano en un solo archivo Markdown (.md).")

# Verificar si el entorno es local o en la nube (usamos la variable de secretos de Streamlit Cloud)
if os.getenv("STREAMLIT_CLOUD", False):  # Detectar si estamos en la nube
    # En la nube, usamos la carpeta temporal
    output_folder = tempfile.gettempdir()
    st.write(f"Los archivos se guardarán en un directorio temporal: {output_folder}")

else:
    # En local, permitimos que el usuario elija la ruta de salida
    output_folder = st.text_input("Introduce la ruta de la carpeta de salida:", value=os.getcwd()) # Input para la ruta de salida
    st.session_state['output_folder'] = output_folder  # Guardar en session_state

# Checkbox para decidir si sobrescribir el archivo existente
overwrite = st.checkbox("Sobrescribir 'Documentación_indexada.md' si existe", value=False) # Checkbox para sobrescribir

# Cargador de archivos
st.header("Carga de Archivos") # Título de la sección
uploaded_files = st.file_uploader( # Cargador de archivos
    "Introduce tus archivos de texto", 
    type=['md', 'txt', 'py', 'js'], 
    accept_multiple_files=True # Permitir subir varios archivos a la vez (tengo que probarlo)
)

# Botón para iniciar el proceso
if st.button("Procesar Archivos"): # Botón para procesar los archivos subidos
    if uploaded_files and output_folder: # Si hay archivos subidos y se ha introducido la ruta de salida
        # Verificar si la carpeta de salida existe (solo en local)
        if not os.path.isdir(output_folder): # Si la carpeta de salida no existe
            st.error(f"La carpeta {output_folder} no existe.") # Mostrar mensaje de error
        else:
            # Ruta del archivo de salida
            output_file_path = os.path.join(output_folder, "Documentación_indexada.md") # Ruta del archivo de salida

            # Seleccionar modo de escritura
            mode = 'w' if overwrite else 'a' # Modo de escritura: 'w' para sobrescribir, 'a' para añadir

            # Abrir el archivo de salida
            with open(output_file_path, mode, encoding='utf-8') as outfile: # Abrir el archivo de salida en modo de escritura
                for uploaded_file in uploaded_files: # Iterar sobre los archivos subidos
                    # Leer el contenido del archivo subido
                    content = uploaded_file.read().decode('utf-8') # Leer el contenido del archivo subido y decodificarlo

                    # Escribir separador y nombre del archivo
                    separator = f"\n\n---\n\n# Contenido de {uploaded_file.name}\n\n" # Separador y nombre del archivo
                    outfile.write(separator) # Escribir el separador y el nombre del archivo en el archivo de salida

                    # Escribir el contenido
                    outfile.write(content) # Escribir el contenido del archivo subido en el archivo de salida 

                    # Mostrar mensaje de éxito
                    st.success(f"Se ha agregado el contenido de {uploaded_file.name} a 'Documentación_indexada.md'.")   

            st.info(f"El archivo 'Documentación_indexada.md' ha sido actualizado en {output_folder}.") # Mostrar mensaje de información

            # Mostrar el enlace para descargar el archivo resultante
            with open(output_file_path, "rb") as f: # Abrir el archivo de salida en modo binario para poder descargarlo
                st.download_button( # Botón para descargar el archivo
                    label="Descargar el archivo concatenado", # Etiqueta del botón
                    data=f, # Datos a descargar (el archivo de salida)
                    file_name="Documentación_indexada.md", # Nombre del archivo a descargar 
                    mime="text/markdown" # Tipo MIME del archivo a descargar
                )
    else:
        st.warning("Por favor, introduce la ruta de la carpeta de salida y selecciona al menos un archivo .md o .txt.")
### Fin del script ###