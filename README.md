# SISTEMA DE GENERACIÓN DE REPORTES Y GRÁFICOS DE LAS ESTACIONES

Este es un proyecto desarrollado en Python, la finalidad del aplicativo es facilitar la gestión de la información de las estaciones de la red de monitoreo dentro del Sistema de Información de Instrumentación de Geoamenazas (SIIGeo).

## Instalación

Para instalar este proyecto y las librerías necesarias, sigue estos pasos:

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python `3.12.0` o superior instalado en tu sistema.
3. Crea un entorno virtual utilizando `venv` o `conda`.
4. Activa el entorno virtual.
5. Ejecuta el comando `pip install -r requirements.txt` para instalar las librerías necesarias.

## Ejecución del aplicativo
Para correr este proyecto:

1. Activa el entorno virtual que se creo en la sección anterior.
2. Ejecuta el comando `streamlit run 1_Reporte general de las estaciones.py`, el aplicativo generara una vista como esta:
![Captura](https://github.com/CristianDavid313/Aplicativo/assets/140470836/1e3963e2-e097-4c1c-8093-ac98640d6b0f)
3. Se generaran 2 rutas, a la ruta `Local URL` solo se puede acceder desde el mismo dispositivo en el que se está ejecutando la aplicación. Por otro lado, a la ruta `Network URL` solo se puede acceder si el dispositivo está conectado a la misma red en la que se encuentra el dispositivo que está ejecutando la aplicación.

¡Disfruta de mi proyecto Python!
