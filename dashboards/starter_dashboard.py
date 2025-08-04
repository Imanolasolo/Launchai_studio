import streamlit as st
import base64
from datetime import datetime
# Importar la función del curso
from courses.Curso_Agencia_starter_IA.curso1 import run_curso

def starter_dashboard(user):
    # Sidebar de navegación
    st.sidebar.subheader("Starter")
    selected = st.sidebar.radio(
        "Navegación",
        ["Tutoriales", "Cursos", "Herramientas esenciales"],
        key="starter_nav"
    )

    st.title("Panel Starter")
    st.write(f"Bienvenido, {user['full_name']} 🚀")

    if selected == "Tutoriales":
        st.header("Tutoriales")
        st.info("Aquí encontrarás tutoriales introductorios de IA y la plataforma.")
        pdfs = {
            "Tutorial 1: Dominando la IA": "courses/Dominando la IA.pdf",
            "Tutorial 2: Estrategias avanzadas de IA": "assets/pdfs/Estrategias avanzadas de IA.pdf"
        }
        selected_pdf = st.selectbox("Selecciona un tutorial para leer:", list(pdfs.keys()))
        if st.button("Ver PDF"):
            with open(pdfs[selected_pdf], "rb") as f:
                pdf_bytes = f.read()
                st.download_button(
                    label=f"Descargar {selected_pdf}",
                    data=pdf_bytes,
                    file_name=selected_pdf.replace(" ", "_").lower() + ".pdf",
                    mime="application/pdf"
                )
            base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    elif selected == "Cursos":
        st.header("Cursos")
        st.info("Acceso a cursos básicos para comenzar en IA.")
        # Insertar el curso "Curso IA para agencias"
        cursos = [
            "Curso IA para agencias",
            # Puedes agregar más cursos aquí si lo deseas
        ]
        selected_curso = st.selectbox("Selecciona un curso:", cursos)
        if selected_curso == "Curso IA para agencias":
            run_curso()
        # ...puedes agregar lógica para otros cursos aquí...

    elif selected == "Herramientas esenciales":
        st.header("Herramientas esenciales")
        st.info("Recursos y herramientas esenciales para tus primeros proyectos de IA.")
        col1,col2 = st.columns(2)
        with col1:
            with st.expander("Doc4Chat", expanded=False):
                st.markdown("""
                Doc4Chat es una herramienta para interactuar con documentos PDF de manera intuitiva.
                """)
        with col2:
            with st.expander("Knowledge Base Builder", expanded=False):
                st.markdown("""
                Knowledge Base Builder es una herramienta para crear bases de conocimiento tipo plan de negocio a partir de una idea.
                """)
        herramienta = st.selectbox("Selecciona una herramienta:", ["Doc4Chat", "Knowledge Base Builder"])
        if herramienta == "Doc4Chat":
            st.markdown(
                """
                <a href="https://doc4chat.streamlit.app/?embed_options=dark_theme" target="_blank">
                    <button style="background-color:#25D366;color:white;border:none;padding:10px 24px;border-radius:5px;font-size:16px;cursor:pointer;">
                        Abrir Doc4Chat
                    </button>
                </a>
                """,
                unsafe_allow_html=True
            )
        elif herramienta == "Knowledge Base Builder":
            st.markdown(
                """
                <a href="https://knowledge-base-constructor.streamlit.app/">
                    <button style="background-color:#25D366;color:white;border:none;padding:10px 24px;border-radius:5px;font-size:16px;cursor:pointer;">
                        Abrir Knowledge Base Builder
                    </button>
                </a>
                """,
                unsafe_allow_html=True
            )


