# dashboards/pro_builder_dashboard.py
import streamlit as st
from datetime import datetime
import uuid
import base64

def pro_builder_dashboard(user):
    # Sidebar de navegación
    st.sidebar.subheader("Pro Builder")
    selected = st.sidebar.radio(
        "Navegación",
        ["Dashboard", "Mis Proyectos", "Cursos Avanzados", "Herramientas Pro", "Marketplace"],
        key="pro_builder_nav"
    )

    st.title("👷 Pro Builder Dashboard")
    st.write(f"Bienvenido, {user['full_name']} 🛠️")

    if selected == "Dashboard":
        st.info("Panel principal con estadísticas y resumen de proyectos.")
        # ...existing dashboard code...
        
    elif selected == "Mis Proyectos":
        st.markdown("## 📦 Mis Proyectos")
        # Simulación temporal con session_state (puedes conectar esto a SQLite después)
        if "pro_projects" not in st.session_state:
            st.session_state.pro_projects = []

        # Crear nuevo proyecto
        with st.expander("➕ Crear nuevo proyecto", expanded=False):
            with st.form("crear_proyecto"):
                project_name = st.text_input("Nombre del proyecto")
                description = st.text_area("Descripción del proyecto")
                project_type = st.selectbox("Tipo de proyecto", [
                    "Chatbot IA", "Generador de Contenido", "Clasificador de Datos", "Automatización", "Otro"
                ])
                submitted = st.form_submit_button("Crear proyecto")
                if submitted and project_name:
                    st.session_state.pro_projects.append({
                        "id": str(uuid.uuid4())[:8],
                        "name": project_name,
                        "description": description,
                        "type": project_type,
                        "owner": user["username"],
                        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
                    })
                    st.success("Proyecto creado correctamente ✅")

        # Listado de proyectos
        if st.session_state.pro_projects:
            for project in st.session_state.pro_projects:
                with st.expander(f"📁 {project['name']}"):
                    st.markdown(f"**ID:** `{project['id']}`")
                    st.markdown(f"**Tipo:** {project['type']}")
                    st.markdown(f"**Descripción:** {project['description']}")
                    st.markdown(f"**Creado el:** {project['created']}")
                    st.markdown(f"**Propietario:** {project['owner']}")
                    st.button("🚀 Lanzar", key=f"launch_{project['id']}")
                    st.button("🗑️ Eliminar", key=f"delete_{project['id']}")
        else:
            st.warning("No tienes proyectos creados aún.")

    elif selected == "Cursos Avanzados":
        st.header("🎓 Cursos Avanzados")
        st.info("Cursos especializados para dominar el desarrollo no-code con IA.")
        
        cursos_avanzados = [
            "Arquitectura de Soluciones IA",
            "Automatización Avanzada con IA",
            "Monetización y Escalabilidad",
            "APIs y Integraciones No-Code",
            "Gestión de Proyectos IA"
        ]
        
        selected_curso = st.selectbox("Selecciona un curso avanzado:", cursos_avanzados)
        
        if selected_curso == "Arquitectura de Soluciones IA":
            with st.expander("📚 Contenido del curso", expanded=True):
                st.markdown("""
                **Módulos del curso:**
                1. Diseño de arquitecturas escalables
                2. Selección de herramientas y tecnologías
                3. Patrones de diseño para IA
                4. Casos de estudio reales
                """)
                
        elif selected_curso == "Automatización Avanzada con IA":
            with st.expander("📚 Contenido del curso", expanded=True):
                st.markdown("""
                **Módulos del curso:**
                1. Zapier y Make.com para automatización
                2. Workflows complejos con IA
                3. Integración de múltiples herramientas
                4. Monitoreo y optimización
                """)
                
        elif selected_curso == "Monetización y Escalabilidad":
            with st.expander("📚 Contenido del curso", expanded=True):
                st.markdown("""
                **Módulos del curso:**
                1. Modelos de negocio con IA
                2. Pricing strategies
                3. Escalabilidad técnica y comercial
                4. Métricas y KPIs clave
                """)
                
        elif selected_curso == "APIs y Integraciones No-Code":
            with st.expander("📚 Contenido del curso", expanded=True):
                st.markdown("""
                **Módulos del curso:**
                1. Fundamentos de APIs para no-coders
                2. Integraciones con OpenAI, Google, etc.
                3. Webhooks y automatización
                4. Seguridad y mejores prácticas
                """)
                
        elif selected_curso == "Gestión de Proyectos IA":
            with st.expander("📚 Contenido del curso", expanded=True):
                st.markdown("""
                **Módulos del curso:**
                1. Metodologías ágiles para proyectos IA
                2. Gestión de equipos remotos
                3. Comunicación con clientes
                4. Entrega y mantenimiento
                """)
        
        st.info("💡 Próximamente: Acceso completo a todos los módulos con videos, PDFs y proyectos prácticos.")

    elif selected == "Herramientas Pro":
        st.header("🛠️ Herramientas Pro")
        st.info("Herramientas avanzadas para construir soluciones empresariales.")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("🤖 AI Model Playground", expanded=False):
                st.markdown("""
                Prueba diferentes modelos de IA (GPT-4, Claude, etc.) para encontrar 
                el mejor para tu proyecto específico.
                """)
            with st.expander("📊 Analytics Dashboard", expanded=False):
                st.markdown("""
                Analiza el rendimiento de tus proyectos IA con métricas 
                avanzadas y reportes automáticos.
                """)
                
        with col2:
            with st.expander("🔗 API Manager", expanded=False):
                st.markdown("""
                Gestiona todas tus integraciones API desde un solo lugar, 
                con monitoreo y límites de uso.
                """)
            with st.expander("🎨 UI/UX Builder", expanded=False):
                st.markdown("""
                Constructor visual de interfaces para tus aplicaciones IA 
                sin escribir código.
                """)
        
        herramienta_pro = st.selectbox("Selecciona una herramienta:", 
                                     ["AI Model Playground", "Analytics Dashboard", "API Manager", "UI/UX Builder"])
        
        if herramienta_pro == "AI Model Playground":
            st.info("🚧 En desarrollo - Disponible próximamente")
        elif herramienta_pro == "Analytics Dashboard":
            st.info("🚧 En desarrollo - Disponible próximamente")
        elif herramienta_pro == "API Manager":
            st.info("🚧 En desarrollo - Disponible próximamente")
        elif herramienta_pro == "UI/UX Builder":
            st.info("🚧 En desarrollo - Disponible próximamente")

    elif selected == "Marketplace":
        st.header("🏪 Marketplace")
        st.info("Comparte y monetiza tus proyectos, o descarga plantillas de otros Pro Builders.")
        
        tab1, tab2 = st.tabs(["🛒 Explorar", "💰 Mis Ventas"])
        
        with tab1:
            st.subheader("Plantillas Disponibles")
            
            plantillas = [
                {"nombre": "Chatbot E-commerce", "precio": "$29", "autor": "Builder123"},
                {"nombre": "Sistema de Tickets IA", "precio": "$45", "autor": "AIExpert"},
                {"nombre": "Generador de Contenido", "precio": "$35", "autor": "ContentMaster"},
            ]
            
            for plantilla in plantillas:
                with st.expander(f"🎯 {plantilla['nombre']} - {plantilla['precio']}"):
                    st.write(f"**Autor:** {plantilla['autor']}")
                    st.write("Descripción de la plantilla y sus funcionalidades...")
                    st.button(f"Comprar {plantilla['precio']}", key=f"buy_{plantilla['nombre']}")
        
        with tab2:
            st.subheader("Publica tu plantilla")
            with st.form("publicar_plantilla"):
                nombre_plantilla = st.text_input("Nombre de la plantilla")
                descripcion_plantilla = st.text_area("Descripción")
                precio_plantilla = st.number_input("Precio ($)", min_value=1, value=25)
                archivo_plantilla = st.file_uploader("Subir archivo de plantilla", type=['json', 'zip'])
                
                if st.form_submit_button("Publicar en Marketplace"):
                    st.success("¡Plantilla enviada para revisión!")

