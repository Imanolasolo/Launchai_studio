import streamlit as st
import base64
import os

def render():
    st.title("📘 Módulo 1: El potencial de la IA para tu agencia")
    st.markdown("### 🎯 Objetivo del módulo")
    st.write("Comprender qué es la inteligencia artificial, cómo está transformando los negocios y por qué es una gran oportunidad para crear una agencia de herramientas IA.")

    st.markdown("### 📚 Aprenderás a:")
    st.markdown("""
    - Entender los fundamentos de la IA (explicado en lenguaje simple).
    - Identificar oportunidades reales de negocio con IA.
    - Conocer ejemplos de soluciones simples sin saber programar.
    - Visualizar tu futuro como creador/a de herramientas con IA.
    """)

    st.divider()

    with st.expander("🎥 Video: ¿Por qué ahora es el momento de crear con IA?"):
        video_path = "assets/videos/modulo1.mp4"
        if os.path.exists(video_path):
            st.video(video_path)
        else:
            st.warning("⚠️ Video no encontrado. Asegúrate de subir el archivo `modulo1.mp4` a `assets/videos/`")

    st.divider()

    with st.expander("📄 Descarga y visualiza el PDF del Módulo"):
        pdf_path = "assets/pdfs/Modulo1_AgenciaIA.pdf"
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
            with open(pdf_path, "rb") as f:
                st.download_button(label="📥 Descargar PDF del Módulo 1", data=f, file_name="modulo1.pdf", mime="application/pdf")
        else:
            st.warning("⚠️ PDF no encontrado. Asegúrate de subir el archivo `modulo1.pdf` a `assets/pdfs/`")

    st.divider()

    st.success("¡Listo! Puedes continuar con el Módulo 2 desde el menú lateral.")

