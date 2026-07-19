"""
ui/chat.py

Componente visual del Chat con el Dataset.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st


class Chat:
    """
    Interfaz del Chat IA.
    """

    @staticmethod
    def render(app):

        st.divider()

        st.subheader("💬 Chat con el Dataset")

        st.caption(
            "Haz preguntas en lenguaje natural sobre tus datos."
        )

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        with st.expander("💡 Ejemplos de preguntas"):

            st.markdown("""
- ¿Cuántas filas tiene el dataset?
- ¿Cuántas columnas tiene?
- ¿Cuántos valores nulos existen?
- ¿Cuáles son las variables numéricas?
- ¿Cuál es el promedio de Ventas?
- ¿Cuál es el máximo de Ventas?
- ¿Cuál es el promedio de Utilidad?
- ¿Cuál es el máximo de Margen?
""")

        # Mostrar historial
        for item in st.session_state.chat_history:

            st.markdown(f"**👤 Tú:** {item['question']}")
            st.markdown(f"**🤖 IA:** {item['answer']}")
            st.divider()

        question = st.text_input(
            "Pregunta",
            placeholder="Ejemplo: ¿Cuál es el promedio de Ventas?",
            key="chat_input_v2",
        )

        if st.button(
            "🚀 Preguntar",
            key="chat_button_v2",
            use_container_width=True,
        ):

            if not question.strip():
                st.warning("Escribe una pregunta.")
                return

            answer = app.ask(question)

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer,
                }
            )

            st.rerun()