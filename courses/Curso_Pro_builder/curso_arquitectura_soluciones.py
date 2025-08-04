import streamlit as st

st.set_page_config(page_title="Curso: Arquitectura de Soluciones IA", layout="wide")
st.title("🧠 Curso: Arquitectura de Soluciones IA")
st.markdown("Aprende a construir soluciones escalables, seguras y profesionales con IA.")

st.info("✅ Este curso está diseñado para builders que quieren dominar la arquitectura técnica de productos de IA.")

# MÓDULO 1
with st.expander("📘 Módulo 1: Diseño de Arquitecturas Escalables", expanded=True):
    st.subheader("Objetivo:")
    st.write("Comprender cómo diseñar soluciones de IA que puedan escalar técnica y comercialmente.")

    st.markdown("""
    ### 🔍 ¿Qué es una arquitectura escalable?

    Una arquitectura escalable es capaz de manejar un crecimiento sostenido del sistema sin perder rendimiento. 
    En el contexto de soluciones IA, esto significa que el sistema puede atender a más usuarios, procesar más datos 
    o incorporar nuevas funcionalidades sin requerir una reestructuración completa.

    #### Tipos de arquitectura:

    - **Monolítica:** Todo el sistema está en un solo bloque. Fácil de comenzar pero difícil de escalar.
    - **Microservicios:** Se divide en pequeños servicios independientes. Ideal para escalar, mantener y desplegar por partes.
    - **Serverless:** Ideal para cargas intermitentes. Puedes usar servicios como AWS Lambda, Firebase Functions, etc.

    👉 Las soluciones modernas tienden a utilizar **microservicios** combinados con APIs, bases de datos escalables y herramientas en la nube.
    """)

    with st.form("modulo_1_form"):
        st.markdown("### 🧪 Ejercicio: ¿Qué tipo de arquitectura usarías para un asistente que atienda a 1000 usuarios a la vez?")
        arquitectura = st.radio("Selecciona una opción:", [
            "Monolítica",
            "Modular con microservicios",
            "Script único en un servidor local"
        ])
        submitted = st.form_submit_button("Enviar respuesta")
        if submitted:
            if arquitectura == "Modular con microservicios":
                st.success("✅ ¡Correcto! Este modelo permite escalar fácilmente.")
            else:
                st.warning("❌ Revisa el concepto de escalabilidad y vuelve a intentarlo.")

# MÓDULO 2
with st.expander("📘 Módulo 2: Selección de Herramientas y Tecnologías"):
    st.subheader("Objetivo:")
    st.write("Aprender a elegir la herramienta adecuada según el tipo de proyecto IA que estás construyendo.")

    st.markdown("""
    ### 🧰 ¿Cómo elegir la herramienta correcta?

    No necesitas saber programar para construir soluciones IA si eliges bien tus herramientas:

    - **Automatización sin código:** [Make](https://www.make.com), [Zapier](https://zapier.com) te permiten conectar apps sin escribir código.
    - **Interfaz visual:** [Webflow](https://webflow.com), [Bubble](https://bubble.io) permiten diseñar frontends visuales para apps IA.
    - **IA generativa:** APIs como OpenAI, Anthropic o Cohere ofrecen modelos listos para generar texto, imágenes, etc.
    - **Persistencia y datos:** Airtable, Firebase, Supabase son opciones viables sin código para manejar datos.

    ✅ Elegir bien es clave para evitar sobrecostos, lentitud o proyectos frágiles.
    """)

    st.markdown("### 🧪 Ejercicio interactivo")
    col1, col2 = st.columns(2)
    with col1:
        herramienta = st.selectbox("¿Qué herramienta usarías para automatizar flujos sin código?", 
                                   ["LangChain", "Make", "OpenAI API", "Python puro"])
    with col2:
        uso = st.selectbox("¿Y cuál usarías para personalizar la interfaz visual para el cliente?",
                           ["Firebase", "Webflow", "GPT-4", "Zapier"])
    
    if st.button("Evaluar selección"):
        if herramienta == "Make" and uso == "Webflow":
            st.success("✅ Muy bien, son herramientas ideales para automatización y front sin código.")
        else:
            st.error("❌ Intenta identificar bien el propósito de cada herramienta.")

# MÓDULO 3
with st.expander("📘 Módulo 3: Patrones de Diseño para IA"):
    st.subheader("Objetivo:")
    st.write("Aplicar patrones probados como RAG, agentes LLM y orquestadores para construir soluciones más robustas.")

    st.markdown("""
    ### 🧠 Principales patrones de diseño en IA:

    - **RAG (Retrieval-Augmented Generation):** Busca información relevante (base de datos, PDFs, etc.) y luego genera una respuesta. Ejemplo: Chatbot con conocimiento empresarial.
    - **Agentes Orquestados:** Un modelo toma decisiones y llama a distintas funciones para lograr un objetivo. Ejemplo: AI que agenda citas, responde emails, y busca info.
    - **Pipeline de procesamiento:** Serie de pasos (limpieza → análisis → respuesta) que se ejecutan secuencialmente.

    Estos patrones mejoran la **precisión**, **control** y **personalización** de tus soluciones.

    """)

    st.markdown("### 🧪 Quiz: ¿Cuál es la principal ventaja del patrón RAG?")
    respuesta_rag = st.radio("Selecciona la correcta:", [
        "Permite diseñar una interfaz más bonita",
        "Combina recuperación de datos con generación de texto",
        "Mejora el costo de la API",
        "Evita usar inteligencia artificial"
    ])

    if st.button("Comprobar respuesta"):
        if respuesta_rag == "Combina recuperación de datos con generación de texto":
            st.success("✅ ¡Correcto! RAG permite generar respuestas basadas en información externa.")
        else:
            st.warning("❌ No es correcto. Piensa en cómo se usa RAG para mejorar las respuestas de un LLM.")

# MÓDULO 4
with st.expander("📘 Módulo 4: Casos de Estudio Reales"):
    st.subheader("Objetivo:")
    st.write("Estudiar soluciones reales y aprender de sus arquitecturas para aplicarlas en tus propios proyectos.")

    st.markdown("""
    ### 📂 Casos reales:

    - **Chatbot legal para empleados:** Usa OpenAI + ChromaDB (base vectorial) + interfaz en Streamlit. Incluye control de accesos y logs de auditoría.
    - **Generador de contenido para redes sociales:** Usa GPT-4 + plantillas + exportación automática a redes vía Zapier.
    - **Sistema de clasificación de tickets:** Clasifica con IA + agrupa por tema + presenta dashboard para priorización de soporte.

    """)

    st.markdown("### 🧪 ¿Cuál de estos casos se parece más a tu proyecto?")
    casos = st.radio("Elige uno:", [
        "Chatbot legal con base interna",
        "Generador de campañas para redes sociales",
        "Sistema de análisis de tickets de soporte"
    ])

    if st.button("Ver recomendaciones"):
        if casos == "Chatbot legal con base interna":
            st.info("👉 Usa RAG, bases vectoriales como FAISS o ChromaDB y autenticación segura.")
        elif casos == "Generador de campañas para redes sociales":
            st.info("👉 Usa GPT-4 Turbo, templates personalizables y salida hacia APIs de redes.")
        else:
            st.info("👉 Usa clasificación con IA, etiquetas automáticas y dashboards con métricas.")

# FINAL
st.success("🎯 ¡Has completado los módulos interactivos! Sigue construyendo con propósito.")
