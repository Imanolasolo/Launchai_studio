# curso1.py
import streamlit as st
from courses.Curso_Agencia_starter_IA.modules import module1, module2, module3, module4
import os

def run_curso():

    st.sidebar.title("🚀 Curso Agencia de IA")
    seleccion = st.sidebar.radio(
        "Ir al módulo:",
        ("🏠 Bienvenida", "📘 Módulo 1", "🛠️ Módulo 2", "📦 Módulo 3", "🎁 Módulo 4")
    )

    st.markdown("<style> .block-container { padding-top: 1rem; } </style>", unsafe_allow_html=True)

    if seleccion == "🏠 Bienvenida":
        st.title("Bienvenido al Curso: Agencia de Herramientas con IA")
        portada_path = "assets/images/portada.jpg"
        if os.path.exists(portada_path):
            st.image(portada_path, width=100)
        else:
            st.image("https://em-content.zobj.net/source/microsoft-teams/363/rocket_1f680.png", use_column_width=True)
        st.markdown("""
        Este curso está diseñado para ayudarte a crear tu propia agencia de herramientas basadas en IA, sin necesidad de saber programar.

        **Estructura del curso:**
        - 4 módulos prácticos.
        - Videos explicativos cortos.
        - PDFs descargables.
        - Plantillas listas para usar.

        Usa el menú de la izquierda para comenzar 👉
        """)
        st.success("Cuando estés listo, haz clic en el Módulo 1 en la barra lateral.")

    elif seleccion == "📘 Módulo 1":
        module1.render()

    elif seleccion == "🛠️ Módulo 2":
        module2.render()

    elif seleccion == "📦 Módulo 3":
        module3.render()

    elif seleccion == "🎁 Módulo 4":
        module4.render()