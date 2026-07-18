"""
ui/chat.py

Componente de conversación con el dataset.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st


class Chat:
    """
    Interfaz del Chat con el Dataset.
    """

    @staticmethod
    def render(app):

        st.subheader("💬 Chat con el Dataset")

        st.caption(
            "Haz preguntas sobre el dataset utilizando lenguaje natural."
        )

        question = st.text_input(
            "Pregunta",
            placeholder="Ejemplo: ¿Cuántas filas tiene el dataset?",
            key="dataset_chat_question",
        )

        col1, col2 = st.columns([1, 4])

        with col1:

            ask = st.button(
                "Preguntar",
                width="stretch",
            )

        with col2:

            clear = st.button(
                "Limpiar",
                width="stretch",
            )

        if clear:

            st.session_state.dataset_chat_question = ""

            st.rerun()

        if ask:

            if not question.strip():

                st.warning(
                    "Escribe una pregunta."
                )

                return

            with st.spinner(
                "Consultando el Analista IA..."
            ):

                answer = app.ask(question)

            st.markdown("---")

            st.markdown("### 🤖 Respuesta")

            st.write(answer)