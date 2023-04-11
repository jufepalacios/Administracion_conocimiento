import streamlit as st

st.set_page_config(
    page_title="Bavaria",
    page_icon=":beer:",
)

st.write("# Data for Marketing :chart_with_upwards_trend: - Onboarding")

st.sidebar.info("Seleccione un curso de los disponibles arriba.")

st.markdown(
    """
    #### Hola!
    Bienvenido al proceso de Onboarding de AB InBev - Bavaria :beer:

    Esta aplicación tiene como fin entrenarte como nuevo integrante del area de Data for Marketing.

    Para esto, cuentas con los siguientes cursos que podras visualizar y seleccionar en la parte izquierda:
    - Google Cloud.
    - CDP - Customer Data Plataform.

    ***Recuerda que para continuar con las tematicas de cada curso debes ir aprobando una serie de cuestionarios que
    te realizaremos a medida que vas avazando en los cursos.***

    #### Exitos en este nuevo reto!
"""
)