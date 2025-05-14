# app.py

# ====================
# 1. IMPORTAR LIBRERÍAS NECESARIAS
# ====================
# Estas librerías permiten: leer datos (pandas), crear gráficos (plotly) y mostrar contenido web interactivo (streamlit).
import streamlit as st
import pandas as pd
import plotly.express as px

# ====================
# 2. CARGAR LOS DATOS DEL CSV EN UN DATAFRAME
# ====================
# Esta línea lee el archivo CSV que contiene los datos sobre autos.
datos_vehiculos = pd.read_csv('vehicles_us.csv')

# ====================
# 3. ENCABEZADO DE LA APLICACIÓN
# ====================
# Esto aparece al principio de la página web como título.
st.header('Análisis de Datos de Vehículos en Venta')

# ====================
# 4. DESCRIPCIÓN EXPLICATIVA PARA LOS USUARIOS
# ====================
st.write('''
Esta es una aplicación interactiva creada con **Streamlit** para visualizar datos de automóviles disponibles para la venta.
Puedes seleccionar los gráficos que deseas ver marcando las opciones a continuación.
''')

# ====================
# 5. CHECKBOX PARA HISTOGRAMA
# ====================
boton_histograma = st.checkbox('Mostrar histograma del kilometraje (odómetro)')

# Si el usuario marca esta casilla, se muestra el histograma
if boton_histograma:
    st.write('Creando histograma del kilometraje recorrido por los autos (odómetro).')
    fig_hist = px.histogram(datos_vehiculos,
                            x='odometer',
                            nbins=50,
                            title='Distribución del Kilometraje (Odómetro)')
    # Ajustar etiquetas de los ejes
    fig_hist.update_layout(
        xaxis_title='Millas recorridas',
        yaxis_title='Cantidad de autos'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# ====================
# 6. CHECKBOX PARA GRÁFICO DE DISPERSIÓN
# ====================
boton_dispersion = st.checkbox('Mostrar gráfico de dispersión: Odómetro vs Precio')

# Si el usuario marca esta casilla, se muestra el gráfico de dispersión
if boton_dispersion:
    st.write('Creando gráfico de dispersión para observar relación entre kilometraje y precio.')
    fig_disp = px.scatter(datos_vehiculos,
                          x='odometer',
                          y='price',
                          title='Relación entre Kilometraje y Precio')
    fig_disp.update_layout(
        xaxis_title='Millas recorridas',
        yaxis_title='Precio en dólares'
    )
    st.plotly_chart(fig_disp, use_container_width=True)

# ====================
# FIN DEL CÓDIGO