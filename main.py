### Este script permite concatenar archivos Markdown y Texto en un solo archivo Markdown. Lo he hecho para obtener la documentación ###
### de un proyecto en un solo archivo para poder entrenar un RAG. Aunque no es fundamental el tener la documentación ordenada, sí que es buena práctica ###
### y puede ser útil para otros proyectos. ###
import streamlit as st # Importar la librería Streamlit para crear la aplicación web (la almacenaré en un docker además de en streamlit cloud)
import os # Importar la librería os para trabajar con archivos y directorios
import subprocess # Importar la librería subprocess para ejecutar comandos del sistema operativo
import sys # Importar la librería sys para obtener información del sistema operativo

# Título de la aplicación
st.title("Md Merger by b0rjen")

# Input para la ruta de la carpeta de salida
st.subheader("Esta app permite concatenar archivos de texto plano en un solo archivo Markdown (.md).")
output_folder = st.text_input("Introduce la ruta de la carpeta de salida:", value=os.getcwd())

# Almacenar output_folder en session_state
st.session_state['output_folder'] = output_folder

# Checkbox para decidir si sobrescribir el archivo existente
overwrite = st.checkbox("Sobrescribir 'Documentación_indexada.md' si existe", value=False) # Por defecto, no sobrescribir

# Cargador de archivos
st.header("Carga de Archivos") # Título de la sección
uploaded_files = st.file_uploader( # Cargador de archivos
    "Introduce tus archivos de texto", # Mensaje para el usuario
    type=['md', 'txt', 'py', 'js'], # Tipos de archivos permitidos (Markdown, Texto, Python, JavaScript) vendrán más tipos en la siguiente versión
    accept_multiple_files=True # Permitir la carga de varios archivos
)

# Botón para iniciar el proceso
if st.button("Procesar Archivos"): # Si se pulsa el botón
    if uploaded_files and output_folder: # Si se han subido archivos y se ha introducido la ruta de la carpeta de salida
        # Verificar si la carpeta de salida existe
        if not os.path.isdir(output_folder):
            st.error(f"La carpeta {output_folder} no existe.")
        else:
            # Ruta del archivo de salida
            output_file_path = os.path.join(output_folder, "Documentación_indexada.md") # Nombre del archivo de salida (se queda así fijo)

            # Almacenar output_file_path en session_state
            st.session_state['output_file_path'] = output_file_path # Almacenar la ruta del archivo de salida en la sesión

            # Seleccionar modo de escritura
            mode = 'w' if overwrite else 'a' # Si se ha marcado la casilla de sobrescribir, se sobrescribirá el archivo; si no, se añadirá al final

            # Abrir el archivo de salida
            with open(output_file_path, mode, encoding='utf-8') as outfile: # Abrir el archivo de salida en modo escritura o añadir
                for uploaded_file in uploaded_files:
                    # Leer el contenido del archivo subido
                    content = uploaded_file.read().decode('utf-8') # Leer el contenido del archivo subido y decodificarlo a UTF-8 para evitar errores

                    # Escribir separador y nombre del archivo
                    separator = f"\n\n---\n\n# Contenido de {uploaded_file.name}\n\n" # Separador y nombre del archivo para identificarlo
                    outfile.write(separator) # Escribir el separador y el nombre del archivo en el archivo de salida

                    # Escribir el contenido
                    outfile.write(content) # Escribir el contenido del archivo subido en el archivo de salida (Documentación_indexada.md)

                    # Mostrar mensaje de éxito
                    st.success(f"Se ha agregado el contenido de {uploaded_file.name} a 'Documentación_indexada.md'.") # Mostrar mensaje de éxito en la interfaz

            st.info(f"El archivo 'Documentación_indexada.md' ha sido actualizado en {output_folder}.") # Mostrar mensaje informativo en la interfaz con la ruta de la carpeta de salida

            # Establecer bandera para mostrar el botón "Abrir Carpeta"
            st.session_state['show_open_folder_button'] = True # Establecer la bandera para mostrar el botón "Abrir Carpeta" en la interfaz
    else:
        st.warning("Por favor, introduce la ruta de la carpeta de salida y selecciona al menos un archivo .md o .txt.") # Mostrar mensaje de advertencia en la interfaz

# Mostrar el botón "Abrir Carpeta" si corresponde
if st.session_state.get('show_open_folder_button', False): # Si la bandera para mostrar el botón "Abrir Carpeta" está activada
    if st.button("Abrir Carpeta"): # Si se pulsa el botón "Abrir Carpeta" en la interfaz de usuario
        output_folder = st.session_state.get('output_folder', None) # Obtener la ruta de la carpeta de salida de la sesión
        if output_folder: # Si se ha introducido la ruta de la carpeta de salida
            try: # Intentar abrir la carpeta de salida
                if sys.platform.startswith('win'): # Si el sistema operativo es Windows (comienza con 'win')
                    os.startfile(output_folder) # Abrir la carpeta de salida en Windows con el comando startfile
                elif sys.platform == 'darwin': # Si el sistema operativo es macOS (Darwin) 
                    subprocess.Popen(['open', output_folder]) # Abrir la carpeta de salida en macOS con el comando open
                else: # Para otros sistemas operativos (Linux, etc.) 
                    subprocess.Popen(['xdg-open', output_folder]) # Abrir la carpeta de salida en otros sistemas operativos con el comando xdg-open
            except Exception as e: # Capturar cualquier excepción que ocurra al abrir la carpeta de salida
                st.error(f"No se pudo abrir la carpeta: {e}") # Mostrar mensaje de error en la interfaz si no se pudo abrir la carpeta
        else: # Si no se ha introducido la ruta de la carpeta de salida
            st.error("No se pudo determinar la carpeta de salida.") # Mostrar mensaje de error en la interfaz si no se pudo determinar la carpeta de salida
### Fin del script ###