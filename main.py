import streamlit as st
from dbconfig import initialize_database, get_connection
from dashboards.starter_dashboard import starter_dashboard
from dashboards.pro_builder_dashboard import pro_builder_dashboard
from datetime import datetime

st.set_page_config(page_title="LaunchAI Studio", page_icon="🚀", layout="wide")

# Dashboards por rol
def dashboard_pro_builder(user):
    st.title("Panel Pro Builder")
    st.write(f"Bienvenido, {user['full_name']} 🛠️")
    pro_builder_dashboard(user)

def dashboard_agency(user):
    st.title("Panel Agency")
    st.write(f"Bienvenido, {user['full_name']} 🏢")
    st.info("Gestión de equipos, clientes y despliegue de soluciones IA.")

def dashboard_white_label(user):
    st.title("Panel White Label")
    st.write(f"Bienvenido, {user['full_name']} 🤝")
    st.info("Personalización total y gestión multi-marca de la plataforma.")

def dashboard_admin(user):
    st.title("Panel Administrador")
    st.write(f"Bienvenido, {user['full_name']} 👑")
    st.info("Gestión global de usuarios, roles y métricas.")

    st.subheader("Gestión de Usuarios")
    conn = get_connection()
    cursor = conn.cursor()
    # Leer usuarios
    cursor.execute("SELECT id, username, role, full_name, email FROM users")
    users = cursor.fetchall()
    user_cols = ["ID", "Usuario", "Rol", "Nombre", "Email"]
    st.table([dict(zip(user_cols, u)) for u in users])

    st.markdown("---")
    st.subheader("Crear nuevo usuario")
    with st.form("crear_usuario"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        full_name = st.text_input("Nombre completo")
        email = st.text_input("Email")
        cursor.execute("SELECT name FROM roles WHERE name != 'admin'")
        roles = [row[0] for row in cursor.fetchall()]
        role = st.selectbox("Rol", roles)
        submitted = st.form_submit_button("Crear usuario")
        if submitted:
            try:
                cursor.execute(
                    "INSERT INTO users (username, password, role, full_name, email) VALUES (?, ?, ?, ?, ?)",
                    (username, password, role, full_name, email)
                )
                conn.commit()
                st.success("Usuario creado correctamente.")
                st.experimental_rerun()
            except Exception as e:
                st.error("Error al crear usuario. ¿Usuario ya existe?")

    st.markdown("---")
    st.subheader("Editar o eliminar usuario")
    cursor.execute("SELECT id, username FROM users WHERE username != 'admin'")
    user_options = cursor.fetchall()
    if user_options:
        selected = st.selectbox("Selecciona usuario", user_options, format_func=lambda x: x[1])
        if selected:
            cursor.execute("SELECT username, role, full_name, email FROM users WHERE id=?", (selected[0],))
            u = cursor.fetchone()
            edit_username = st.text_input("Usuario", value=u[0], key="edit_username")
            edit_full_name = st.text_input("Nombre completo", value=u[2], key="edit_full_name")
            edit_email = st.text_input("Email", value=u[3], key="edit_email")
            cursor.execute("SELECT name FROM roles WHERE name != 'admin'")
            edit_roles = [row[0] for row in cursor.fetchall()]
            edit_role = st.selectbox("Rol", edit_roles, index=edit_roles.index(u[1]), key="edit_role")
            new_password = st.text_input("Nueva contraseña (opcional)", type="password", key="edit_password")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Actualizar usuario"):
                    try:
                        if new_password:
                            cursor.execute(
                                "UPDATE users SET username=?, password=?, role=?, full_name=?, email=? WHERE id=?",
                                (edit_username, new_password, edit_role, edit_full_name, edit_email, selected[0])
                            )
                        else:
                            cursor.execute(
                                "UPDATE users SET username=?, role=?, full_name=?, email=? WHERE id=?",
                                (edit_username, edit_role, edit_full_name, edit_email, selected[0])
                            )
                        conn.commit()
                        st.success("Usuario actualizado.")
                        st.experimental_rerun()
                    except Exception:
                        st.error("Error al actualizar usuario.")
            with col2:
                if st.button("Eliminar usuario"):
                    try:
                        cursor.execute("DELETE FROM users WHERE id=?", (selected[0],))
                        conn.commit()
                        st.success("Usuario eliminado.")
                        st.experimental_rerun()
                    except Exception:
                        st.error("Error al eliminar usuario.")
    conn.close()

# --- Autenticación simple (demo) ---
def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "username": row[1],
            "role": row[3],
            "full_name": row[4] or row[1],
            "email": row[5]
        }
    return None

def landing_page():
    col1, col2 = st.columns([1, 3])
    with col1:  
        st.image("https://em-content.zobj.net/source/microsoft-teams/363/rocket_1f680.png", width=120)
    with col2:
        st.title("Bienvenido a LaunchAI Studio")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("¿Qué es LaunchAI Studio?", expanded=False):
            st.markdown("""
            LaunchAI Studio es una iniciativa educativa y de transformación digital que ayuda a profesionales y empresas a convertirse en agencias de desarrollo y creación de herramientas de Inteligencia Artificial. Nuestra plataforma SaaS te guía paso a paso, desde la formación hasta la creación y despliegue de soluciones IA, sin necesidad de programar.
            """)
    with col2:
        with st.expander("Objetivos de la Iniciativa", expanded=False):
            st.markdown("""
            - Democratizar el acceso a la tecnología y la innovación en IA.
            - Capacitar a individuos y organizaciones para crear y lanzar productos y servicios inteligentes.
            - Fomentar el desarrollo de talento digital y la adopción de herramientas no-code.
            - Impulsar la creación de nuevas agencias y negocios basados en IA.
            """)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Misión", expanded=False):
            st.markdown("""
            Empoderar a la próxima generación de creadores, empresas y agencias para que lideren la transformación digital a través de la Inteligencia Artificial, brindando formación, herramientas y acompañamiento de clase mundial.
            """)
    with col2:
        with st.expander("Visión", expanded=False):
            st.markdown("""
            Ser la plataforma líder en habla hispana para la formación, creación y despliegue de soluciones de IA, facilitando el acceso a la tecnología y el crecimiento de un ecosistema de innovación abierto, inclusivo y sostenible.
            """)
    # Expander centralizado para ayuda de uso, roles y registro
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    col1, col2 = st.columns([3,1])
    with col1:
        with st.expander("ℹ️ ¿Cómo usar esta app? Roles, acceso y registro", expanded=False):
            st.markdown("""
            **¿Cómo funciona LaunchAI Studio?**

            - :blue[**Inicio de sesión:**] Solo los usuarios registrados pueden acceder. Si eres nuevo, contacta al administrador para que cree tu cuenta.
            - :blue[**Roles disponibles:**]
                - :red[**Starter:**] Acceso básico a formación y herramientas introductorias.
                - :red[**Pro Builder:**] Acceso avanzado a creación de proyectos y herramientas no-code.
                - :red[**Agency:**] Gestión de equipos, clientes y despliegue de soluciones IA.
                - :red[**White Label:**] Personalización total y gestión multi-marca.
                - :red[**Admin:**] Gestión de usuarios y administración global.
            - :blue[**Registro:**] El registro de nuevos usuarios solo lo realiza el administrador desde su panel.
            - :blue[**Navegación:**] Una vez dentro, verás un panel adaptado a tu rol con las funcionalidades correspondientes.

            ¿Tienes dudas? Contacta a tu administrador o revisa la documentación interna.
            """)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        # Botón de WhatsApp para registro
        whatsapp_url = "https://wa.me/5930993513082?text=quiero%20registrarme%20en%20LaunchStudio"
        st.markdown(
            f"""
            <div style='display: flex; justify-content: center; margin-bottom: 1em;'>
                <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
                    <button style="background-color:#25D366;color:white;border:none;padding:10px 24px;border-radius:5px;font-size:16px;cursor:pointer;display:flex;align-items:center;gap:8px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp" width="24" height="24">
                        Registrarme por WhatsApp
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
    )
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.info("¿Listo para transformar tu futuro con IA? Inicia sesión para comenzar tu viaje.")
    with col2:
        with st.expander("🔐 Iniciar sesión", expanded=False):
            st.header("Iniciar sesión")
            username = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")
            if st.button("Entrar"):
                user = login(username, password)
                if user:
                    st.session_state.user = user
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas.")

# --- Footer global ---
def show_footer():
    year = datetime.now().year
    st.markdown(
        f"""
        <hr style="margin-top:2em;margin-bottom:0.5em;">
        <div style="text-align:center; color: #888; font-size: 0.95em;">
            Made by <b>CodeCodix AI Lab</b> &nbsp;|&nbsp; {year} &nbsp;|&nbsp; Contacto: <a href="mailto:jjusturi@gmail.com">jjusturi@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- App principal ---
def main():
    initialize_database()
    # Elimina el sidebar de la página principal (solo mostrarlo si hay usuario autenticado)
    if "user" not in st.session_state:
        st.session_state.user = None

    if st.session_state.user:
        st.sidebar.image("https://em-content.zobj.net/source/microsoft-teams/363/rocket_1f680.png", width=80)
        st.sidebar.title("LaunchAI Studio")
        user = st.session_state.user
        st.sidebar.success(f"Sesión: {user['username']} ({user['role']})")
        if st.sidebar.button("Cerrar sesión"):
            st.session_state.user = None
            st.rerun()
        # Dashboards por rol
        if user["role"] == "starter":
            try:
                starter_dashboard(user)
            except FileNotFoundError as e:
                st.error("⚠️ Algunos archivos PDF no están disponibles en esta versión.")
                st.info("Los archivos de formación se están actualizando. Por favor, contacta al administrador.")
                st.write("Error técnico: Archivos PDF no encontrados en el servidor.")
        elif user["role"] == "pro_builder":
            dashboard_pro_builder(user)
        elif user["role"] == "agency":
            dashboard_agency(user)
        elif user["role"] == "white_label":
            dashboard_white_label(user)
        elif user["role"] == "admin":
            dashboard_admin(user)
        else:
            st.error("Rol no reconocido.")
        show_footer()
    else:
        # No sidebar en la página principal
        landing_page()
        show_footer()

if __name__ == "__main__":
    main()
