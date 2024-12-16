# DILVE Data Transformer
 Aplicación para interactuar con la API de DILVE, extrayendo datos bibliográficos y transformándolos en formatos reutilizables como ONIX, CSV, o compatibles con plataformas externas como DSpace o Thoth.
 Esta herramienta está diseñada para facilitar la integración de datos de DILVE (Distribuidor de Información del Libro Español en Venta) con otros sistemas y plataformas. Las principales características incluyen:

Extracción de registros bibliográficos desde DILVE utilizando su API REST.
Transformación de los datos en formatos reutilizables como ONIX 3.1, ONIX 2.1, CSV personalizado, entre otros.
Exportación directa a archivos locales (CSV).
Preparación de datos para su futura integración con plataformas como DSpace y Thoth.
Futuras funcionalidades planeadas:

Envío directo de registros desde DILVE a DSpace.
Integración con la API de Thoth para sincronización de plataformas editoriales.
Soporte para automatización de tareas (extracción programada y envío).
Requisitos:

Python 3.8 o superior.
Dependencias: requests, xml.etree.ElementTree, csv.
Cómo empezar:

Clona este repositorio.
Configura tus credenciales de usuario de DILVE en el archivo de ejemplo.
Ejecuta el script main.py para extraer y procesar datos.
Licencia:
Este proyecto está bajo una licencia abierta para promover la interoperabilidad y el uso eficiente de datos bibliográficos.
