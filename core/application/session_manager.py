"""
core/application/session_manager.py

Administrador del estado de la sesión.

Centraliza toda la información que vive en
st.session_state.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st

from core.application.application_service import (
    ApplicationService,
)


class SessionManager:
    """
    Administra el estado global de Streamlit.
    """

    # =====================================================
    # INICIALIZAR
    # =====================================================

    @staticmethod
    def initialize():

        if "app_service" not in st.session_state:

            st.session_state.app_service = (
                ApplicationService()
            )

        if "analysis_result" not in st.session_state:

            st.session_state.analysis_result = None

        if "chat_history" not in st.session_state:

            st.session_state.chat_history = []

    # =====================================================
    # APPLICATION SERVICE
    # =====================================================

    @staticmethod
    def app():

        return st.session_state.app_service

    # =====================================================
    # ANALYSIS RESULT
    # =====================================================

    @staticmethod
    def analysis_result():

        return st.session_state.analysis_result

    @staticmethod
    def set_analysis_result(result):

        st.session_state.analysis_result = result

    # =====================================================
    # CHAT
    # =====================================================

    @staticmethod
    def chat_history():

        return st.session_state.chat_history

    @staticmethod
    def clear_chat():

        st.session_state.chat_history = []