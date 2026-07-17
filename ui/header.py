"""
ui/header.py

Header principal del Dashboard Enterprise.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st


class Header:
    """
    Renderiza el encabezado principal de la aplicación.
    """

    @staticmethod
    def render() -> None:
        # Título principal
        st.title("🤖 Enterprise AI Data Analyst")

        # Descripción
        st.markdown(
            """
            ### Plataforma Empresarial de Analítica de Datos e Inteligencia Artificial

            Analiza automáticamente datasets, genera dashboards interactivos,
            crea reportes ejecutivos mediante IA y facilita la toma de decisiones
            basada en datos.
            """
        )

        # Línea divisoria
        st.divider()