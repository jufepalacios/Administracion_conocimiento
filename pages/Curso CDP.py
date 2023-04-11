import streamlit as st
from datetime import date
import pandas as pd
import time

today = date.today()

st.set_page_config(page_title="Curso CDP")

st.markdown('# Curso de CDP - Customer Data Plataform')

placeholder = st.empty()
container = placeholder.container()

container.markdown("""

## Modulo 1: CDP - Datos en el CDP

Un récord dentro del CDP se define como un registro de consumidor. Cada récord tiene información ligada que corresponde a un identificador, info demográfica y de marketing. Existen diferentes tipos de records, dependiendo del tipo y cantidad de información que se tenga: 

-	Bronze: No se tiene ninguna información demográfica ni de marketing. Solo de navegación de internet (id cookies, páginas visitadas, dispositivo, navegador usado).  Estos corresponden a usuarios que entraron a una página web o landing page pero no se registraron. 
-	Golden: Se obtiene un identificador (email o teléfono) e información demográfica o de gustos. Corresponden a los consumidores que se registraron en alguna campaña y aceptaron los términos y condiciones para el tratamiento de sus datos. 
-	Diamond: Se tiene información de identificación, demográfica y de compras realizadas. Estos corresponden a los consumidores que han realizado compras dentro de un ecommerce propio de ABInbev. 

Hay diferentes maneras de que la información del cliente entre al CDP:

1.	La navegación de páginas web de las marcas de cervezas o marcas institucionales (Bavaria) y que le usuario acepte explícitamente la recolección de cookies. Si se realiza la conexión correcta con el CDP los datos llegan a este automáticamente. 
2.	Registro en landing pages.  Las landing pages son páginas web sencillas que solo están disponibles temporalmente. Normalmente por el tiempo que dura una campaña. En estas se le solicitan algunos datos al consumidor para el registro.  Si se realiza la conexión correcta con el CDP los datos llegan a este automáticamente.
3.	Formularios de redes sociales. A través de FB se pueden generar encuestas o formularios sencillos, se conocen como leds ads.  Cuando se cierra el formulario, desde FB se puede descargar la data con las respuestas y los datos de los usuarios. Estos datos se pueden subir manualmente al CDP. 
4.	Cuando un cliente realiza la compra de productos o merchandising de una marca a través de uno de los e-commerce de ABInbev. (TaDa, TiendasYa, Colmapp, etc). Para realizar la compra , el usuario debe estar registrado y se le debe solicitar alguna información básica. Esta información llega automáticamente al CDP, la integración se realiza directamente desde el equipo de desarrollo del ecommerce.

""")

container.write(' De acuerdo al texto anterior responda las siguientes preguntas ')

with container.form("form_1"):
   st.markdown("### Pregunta 1")
   option_1 = st.radio(' Si una persona se registró dentro de Tada y agregó items al carro de compras. ¿Qué tipo de record es? ',
             ('a. Bronze',
              'b. Golden',
              'c. Diamond',
              'd. Ruby'))

   submitted = st.form_submit_button("Contestar")
   if submitted:
        if option_1 == 'b. Golden':
            st.success('Respuesta correcta')
        else:
            st.error('Respuesta incorrecta, vuelva a intentarlo')

with container.form("form_2"):
   st.markdown("### Pregunta 2")
   option_2 = st.radio(' Budweiser  lanza una campaña de Leds Ads en FB, y a la semana  de cerrar la campaña no registra ningún récord dentro del CDP. ¿A qué se debe?',
             ('a. Los records de FB no pueden entrar al CDP',
              'b. La carga de estos records se deben realizar manualmente y no se ha realizado.',
              'c. Es necesario esperar un mes para que los records aparezcan.',
              'd. Ninguna de las anteriores.'))

   submitted = st.form_submit_button("Contestar")
   if submitted:
        if option_2 == 'b. La carga de estos records se deben realizar manualmente y no se ha realizado.':
            st.success('Respuesta correcta')
        else:
            st.error('Respuesta incorrecta, vuelva a intentarlo')

if option_1 == 'b. Golden' and option_2 == 'b. La carga de estos records se deben realizar manualmente y no se ha realizado.':
    time.sleep(1)
    placeholder.empty()
    
    container.markdown(' # Muy bien completaste el modulo 1 de este curso.')
