import streamlit as st
import base64

st.set_page_config(page_title="Presentación Módulo 1", layout="centered")

def mostrar_pagina(indice):
    # Muestra el contenido de la "página" según el índice
    if indice == 0:
        st.title("Módulo 1: El potencial de la IA para tu agencia")
        st.write("""
        Bienvenido/a al primer módulo.  
        Hoy descubrirás por qué la inteligencia artificial es la herramienta clave para crear una agencia de soluciones modernas.

        Este módulo es ideal para quienes quieren emprender con IA sin necesidad de programar.
        """)
        col1, col2 = st.columns([1, 2])
        with col2:
            st.image("descarga1.jpg", width=200)
    elif indice == 1:
        st.header("¿Qué es la Inteligencia Artificial (IA)?")
        st.write("""
        La IA es la capacidad de una máquina para aprender de los datos y tomar decisiones o generar contenido por sí sola.

        Tipos más comunes:
        - IA **generativa** (ChatGPT, imágenes, videos).
        - IA **predictiva** (anticipar resultados).
        - IA **automatizadora** (hacer tareas por ti).
        """)
        col1, col2 = st.columns([1, 2])
        with col2:
            st.image("descarga2.jpg", width=200)
    elif indice == 2:
        st.header("¿Por qué es una oportunidad ahora?")
        st.write("""
        - El 80% de empresas quieren integrar IA, pero no saben cómo.
        - Tú puedes ser el puente entre los negocios y las herramientas inteligentes.
        - No necesitas saber código: necesitas entender el valor y empaquetarlo como solución.
        """)
        st.success("Este es el mejor momento para construir con IA.")
        col1, col2 = st.columns([1, 2])
        with col2:
            st.image("descarga3.jpg", width=200)
    elif indice == 3:
        st.header("Ejemplos reales de soluciones simples con IA")
        st.markdown("""
        - **Médico** con chatbot de citas automáticas.  
        - **Coach** que genera planes personalizados con IA.  
        - **Inmobiliaria** que responde consultas automáticamente por WhatsApp.
        """)
        st.info("Estas soluciones puedes ofrecerlas tú, sin programar.")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://images.unsplash.com/photo-1607746882042-944635dfe10e", width=200)
        with col2:
            # Insert a WhatsApp button
            if st.button("Contactar por WhatsApp"):
                whatsapp_link = "https://wa.me/+593993513082"  # Reemplaza con tu número de WhatsApp
                st.markdown(f"[¡Chatea con nosotros! ](https://wa.me/+593993513082)")
    elif indice == 4:
        st.header("Tu futuro como creador/a de herramientas IA")
        st.write("""
        La IA no reemplaza tu trabajo, lo potencia.  
        Con el conocimiento que vas a adquirir, podrás:
        - Crear asistentes virtuales.
        - Automatizar tareas repetitivas.
        - Crear dashboards y reportes con un clic.
        - Vender soluciones a empresas y profesionales.

        ¡Aquí comienza tu camino!
        """)
        st.balloons()

def main():
    if "pagina" not in st.session_state:
        st.session_state.pagina = 0

    total_paginas = 5

    mostrar_pagina(st.session_state.pagina)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.session_state.pagina > 0:
            if st.button("Anterior"):
                st.session_state.pagina -= 1
                st.rerun()
    with col2:
        if st.session_state.pagina < total_paginas - 1:
            if st.button("Siguiente"):
                st.session_state.pagina += 1
                st.rerun()

if __name__ == "__main__":
    main()
    
