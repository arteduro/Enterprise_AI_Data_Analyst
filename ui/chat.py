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

        # ==================================================
        # HISTORIAL
        # ==================================================

        if "chat_history" not in st.session_state:

            st.session_state.chat_history = []

        # ==================================================
        # EJEMPLOS
        # ==================================================

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

        # ==================================================
        # HISTORIAL VISUAL
        # ==================================================

        for question, answer in st.session_state.chat_history:

            with st.chat_message("user"):

                st.write(question)

            with st.chat_message("assistant"):

                st.write(answer)

        # ==================================================
        # INPUT
        # ==================================================

        question = st.chat_input(
            "Escribe una pregunta sobre el dataset..."
        )

        if question:

            answer = app.ask(question)

            st.session_state.chat_history.append(
                (
                    question,
                    answer,
                )
            )

            st.rerun()