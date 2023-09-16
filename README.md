# Organizador de Archivos por Extensiones

Este script Python te permite organizar archivos en una estructura de carpetas basada en sus extensiones.

## Descripción

A menudo, nuestras carpetas se llenan de una variedad de archivos con diferentes extensiones, lo que puede hacer que sea difícil mantener organizados los archivos. Este script resuelve ese problema al automatizar la organización de archivos en carpetas separadas según sus extensiones.

## Complemento para la Gestión de Fotos

Este script se crea con el propósito de mejorar la gestión de fotos al complementar el script anterior. Mientras que el script original se enfoca en organizar archivos por extensiones, este complemento se concentra en facilitar la administración de fotos dentro de las carpetas organizadas.

La combinación de ambos scripts proporciona una solución integral para mantener tus fotos organizadas y accesibles de manera eficiente. El script original se encarga de clasificar los archivos en carpetas según sus extensiones, y este complemento se asegura de que las fotos estén convenientemente etiquetadas y respaldadas, mejorando así la experiencia de gestionar una colección de fotos.

Espero que esta herramienta sea útil para aquellos que buscan una forma más efectiva de gestionar y organizar sus fotos digitales.

Si tienes alguna pregunta o sugerencia para mejorar este complemento o el script original, no dudes en ponerte en contacto conmigo o contribuir al proyecto.


## Uso

### Requisitos previos

- Python 3.x

### Ejecución

1. Clona o descarga este repositorio en tu computadora.
2. Abre una terminal o línea de comandos.
3. Navega al directorio donde se encuentra el script.
4. Ejecuta el script con el siguiente comando:
`python organize_files_by_extension.py`

5. Sigue las instrucciones en la pantalla.

## Configuración Personalizada

Puedes personalizar la configuración del script ajustando la variable `root_folder` en el código para que apunte a tu directorio raíz de archivos. El script creará carpetas separadas en función de las extensiones de los archivos encontrados en esa carpeta raíz.

## Funcionamiento

- El script escanea el directorio raíz y sus subdirectorios en busca de archivos con extensiones.
- Crea carpetas separadas para cada extensión y mueve los archivos a las carpetas correspondientes.
- Si un archivo ya existe en una carpeta específica, se omite y se registra en la salida.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Clona tu repositorio fork en tu máquina local.
3. Crea una nueva rama para tu contribución: `git checkout -b mi-contribucion`.
4. Realiza tus cambios y commitea: `git commit -m "Añade mi contribución"`.
5. Haz un push de tus cambios: `git push origin mi-contribucion`.
6. Crea una solicitud de extracción en GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.




