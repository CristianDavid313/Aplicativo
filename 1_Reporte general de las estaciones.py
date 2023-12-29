import streamlit as st
import pandas as pd
import requests
import os
import errno
from General import Principal

# Configuración inicial del módulo
st.set_page_config(
    page_title = 'Reporte general de las estaciones',
    page_icon = 'Imagenes/Logo.png',
    layout = 'wide',
    initial_sidebar_state='expanded',
    menu_items={
        'About': 'El sistema de generación de reportes y gráficos de las estaciones fue desarrollado por **Cristian David Vargas Avellaneda** con la colaboración del grupo de sismología y el grupo de sistemas. Este aplicativo tiene como objetivo ayudar a los usuarios a comprender las funcionalidades para la gestión de la información de las estaciones de la red de monitoreo dentro del Sistema de Información de Instrumentación de Geoamenazas (SIIGeo). Además, el aplicativo es capaz de generar gráficos y reportes basados en los filtros seleccionados por el usuario, también puede verificar si existen inconsistencias en los datos que están siendo evaluados. **Si encuentra un error la persona que quedara acargo del código sera Angel Daniel Agudelo (adagudelo@sgc.gov.co)**'
    }
)

# Crea la carpeta en la que se guardaran todos los reportes que genere el aplicativo
ruta_actual = os.getcwd()
try:
    os.mkdir('Reportes')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
try:
    os.mkdir('Base')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

st.title('Reporte general de las estaciones', help='Este módulo trabaja con el reporte general de las estaciones en formato ".xlsx", este contiene toda la información de las estaciones de la red de monitoreo')
ruta = 'Base/General.xlsx'

if 'general' not in st.session_state:
    url = requests.get('https://siigeo.sgc.gov.co/stations/staAllExcelView', verify=False)
    open(ruta, 'wb').write(url.content)
    st.session_state['general'] = True

with st.container():
    if ruta is not None:
        df = pd.read_excel(io = ruta)
        df = df.sort_values('IDENTIFICADOR')

        principal = Principal(df)
        st.subheader('Datos cargados:')
        principal.visualizar()

        # Se crean las 4 secciones del módulo
        tab1, tab2, tab3, tab4 = st.tabs(['Reporte general con filtros', 'Estaciones instaladas por año', 'Estaciones retiradas por año', 'Acumulado de estaciones por año'])

        # Sección "Reporte general con filtros"
        with tab1:
            principal.seccion_uno()
            #principal.mapa()
        
        # Sección "Estaciones instaladas por año"
        with tab2:
            principal.seccion_dos()
        
        # Sección "Estaciones instaladas por año"
        with tab3:
            principal.seccion_tres()
        
        # Sección "Acumulado de estaciones por año"
        with tab4:
            principal.seccion_cuatro()
