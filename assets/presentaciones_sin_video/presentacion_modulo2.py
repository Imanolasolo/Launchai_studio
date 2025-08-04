import streamlit as st

st.set_page_config(page_title="Presentación Módulo 2", layout="centered")

def mostrar_pagina(indice):
    if indice == 0:
        st.title("🛠️ Módulo 2: Herramientas IA que puedes usar sin programar")
        st.write("""
        En este módulo conocerás herramientas clave que te permitirán crear soluciones inteligentes,
        sin necesidad de saber programar.

        Desde asistentes virtuales con ChatGPT hasta tus propias bases de conocimiento personalizadas,
        tú puedes empezar hoy mismo.
        """)
        col1, col2 = st.columns([1, 2])
        with col2:
            st.image("NocodeAI.jpg", width=200)

    elif indice == 1:
        st.header("🤖 ChatGPT: el motor detrás de la revolución")
        st.write("""
        ChatGPT es uno de los modelos de lenguaje más potentes hoy.  
        Puedes usarlo para:

        - Atender clientes.
        - Escribir contenido.
        - Automatizar respuestas.
        - Crear interfaces conversacionales.

        Y lo más interesante: puedes 'entrenarlo' con prompts y tus propios datos.
        """)
        col1, col2 = st.columns([1, 2])
        with col2:
            st.image("chatgpt.jpg", width=200)

    elif indice == 2:
        st.header("🗣️ Asistentes Virtuales y Prompt Engineering")
        st.write("""
        Un buen chatbot no responde solo... **responde bien.**

        Por eso necesitas aprender Prompt Engineering y "conectarte" a la IA con una llave propia.

        Un *prompt* es la instrucción que le das al modelo, y dominar eso es como saber programar… pero con lenguaje humano.

        Tu *llave propia (APIKEY)* te permite acceder a la IA de forma personalizada, como si tuvieras un asistente virtual exclusivo. Es la forma que tiene Chatgpt o cualquier IA de saber quién eres y qué necesitas.  

        👉 Tip: Piensa en el chatbot como un empleado. ¿Qué necesitas que haga? ¿Qué tono debe tener? Eso se escribe.
        """)
        col1, col2 = st.columns([1, 2])
        with col2:
            st.image("prompt_engineering.jpg", width=200)

    elif indice == 3:
        st.header("📚 Bases de conocimiento personalizadas")
        st.write("""
        Un paso más allá de los prompts es crear tu propia base de datos con información útil para tu negocio o cliente.

        💡 He creado una herramienta gratuita que te permite crear una base de conocimiento a partir de una idea de negocio en minutos.

        En la barra lateral en herramientas esenciales encontrarás la opción "Base de Conocimiento".  
        Con ella puedes:
        - Crear un archivo PDF con información específica partiendo de una idea de negocio.
        - Ese PDF nos servirá de base de conocimiento para el chat o asistente virtual que utilicemos.
        
        Ideal para: médicos, abogados, agentes inmobiliarios, coaches, etc.
        """)
        
        col1, col2 = st.columns([1, 2])
        with col2:
            st.image("base_conocimiento.jpg", width=200)

    elif indice == 4:
        st.header("📄 Doc4Chat: chatea con un PDF")
        st.write("""
        ¿Y si pudieras subir un documento y conversar con él?

        📄 Con **Doc4Chat** puedes hacerlo.  
        Solo subes un PDF (¿te acuerdas del PDF que hemos creado antes? y el asistente entiende el contenido para responder preguntas, generar resúmenes, contratos, etc.
        
        En la barra lateral en herramientas esenciales encontrarás la opción "Doc4Chat
                 """)        
        col1, col2 = st.columns([1, 2])
        with col2:
            st.image("doc4chat.jpg", width=200)

    elif indice == 5:
        st.header("🧠 Crea tus propias soluciones desde ya")
        st.write("""
        Estás listo para empezar a crear.

        Con:
        - ChatGPT + buenos prompts
        - Tu propio dataset como base de conocimiento
        - Herramientas como Doc4Chat
        - Automatizaciones simples

        🎯 Ya puedes ofrecer tu primera solución como agencia.

        ¡Vamos al próximo módulo!
        """)
        st.balloons()

def main():
    if "pagina_mod2" not in st.session_state:
        st.session_state.pagina_mod2 = 0

    total_paginas = 6
    mostrar_pagina(st.session_state.pagina_mod2)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.session_state.pagina_mod2 > 0:
            if st.button("⬅️ Anterior"):
                st.session_state.pagina_mod2 -= 1
                st.rerun()
    with col2:
        if st.session_state.pagina_mod2 < total_paginas - 1:
            if st.button("Siguiente ➡️"):
                st.session_state.pagina_mod2 += 1
                st.rerun()

if __name__ == "__main__":
    main()
