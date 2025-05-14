Análisis de Datos de Anuncios de Venta de Vehículos
Este proyecto consiste en el análisis exploratorio de un conjunto de datos sobre anuncios de venta de vehículos usados. El objetivo es obtener información clave sobre las características de los vehículos y sus precios.

Aplicación Web Interactiva con Streamlit
Se ha desarrollado una aplicación web simple utilizando la librería Streamlit para permitir una exploración visual interactiva de los datos.

Funcionalidad
La aplicación web proporciona las siguientes funcionalidades:
Carga de Datos: Lee y procesa el conjunto de datos de anuncios de vehículos (vehicles_us.csv).
Visualizaciones Interactivas: Permite al usuario seleccionar qué gráficos desea visualizar mediante casillas de verificación.
Histograma de Kilometraje: Muestra la distribución del kilometraje (odómetro) de los vehículos en el conjunto de datos, permitiendo identificar los rangos de uso más comunes.
Gráfico de Dispersión (Precio vs. Kilometraje): Visualiza la relación entre el precio de venta y el kilometraje de los vehículos, ayudando a identificar tendencias (por ejemplo, si a mayor kilometraje el precio tiende a ser menor) y posibles valores atípicos.
Esta aplicación facilita la comprensión de los datos a través de gráficos interactivos y accesibles desde un navegador web.

Cómo Ejecutar la Aplicación
Para ejecutar esta aplicación web en tu máquina local:
Asegúrate de tener Python y Conda (o un entorno virtual con streamlit, pandas, plotly-express, ipykernel, nbformat) instalados.
Clona este repositorio en tu computadora.
Abre tu Terminal y navega a la carpeta principal del proyecto (donde se encuentra app.py).
Activa tu entorno virtual o de Conda (ej. conda activate vehicles_env).
Ejecuta el comando: streamlit run app.py
La aplicación se abrirá automáticamente en tu navegador web predeterminado.