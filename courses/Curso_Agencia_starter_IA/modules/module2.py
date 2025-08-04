import streamlit as st
import base64
import os

def render():
    st.title("🛠️ Módulo 2: Herramientas No-Code para construir con IA")
    
    st.markdown("### 🎯 Objetivo del módulo")
    st.write(
        "Explorar las herramientas No-Code más utilizadas para crear soluciones con inteligencia artificial "
        "sin necesidad de programar, y cómo combinarlas para crear productos o servicios reales."
    )

    st.markdown("### 📚 Aprenderás a:")
    st.markdown("""
    - Conocer herramientas No-Code clave para IA: generación de texto, imágenes y automatización.
    - Identificar plataformas para construir interfaces y apps sin código.
    - Combinar herramientas para crear soluciones funcionales.
    - Elegir la herramienta correcta según el tipo de problema o cliente.
    """)

    st.divider()

    with st.expander("🎥 Video: Las herramientas No-Code que necesitas dominar"):
        video_path = "assets/videos/modulo2.mp4"
        if os.path.exists(video_path):
            st.video(video_path)
        else:
            st.warning("⚠️ Video no encontrado. Asegúrate de subir el archivo `modulo2.mp4` a `assets/videos/`")

    st.divider()

    with st.expander("📄 Descarga y visualiza el PDF del Módulo"):
        pdf_path = "assets/pdfs/Modulo2_HerramientasNoCode.pdf"
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
            with open(pdf_path, "rb") as f:
                st.download_button(label="📥 Descargar PDF del Módulo 2", data=f, file_name="modulo2.pdf", mime="application/pdf")
        else:
            st.warning("⚠️ PDF no encontrado. Asegúrate de subir el archivo `modulo2.pdf` a `assets/pdfs/`")

    st.divider()

    st.success("¡Bien hecho! Ya puedes pasar al Módulo 3 desde el menú lateral.")
