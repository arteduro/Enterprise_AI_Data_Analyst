"""
ui/sidebar.py

Sidebar principal de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from ui.dataset_panel import DatasetPanel


class Sidebar:
    """
    Barra lateral principal.
    """

    @staticmethod
    def render(
        selected_dataset: Path | None = None,
    ) -> None:

        with st.sidebar:

            # ======================================================
            # CABECERA
            # ======================================================

            st.title("🤖 IA Empresarial")

            st.divider()

            st.subheader("Proyecto")

            st.write("Enterprise AI Data Analyst")

            st.caption(
                "Plataforma de Analítica, IA Generativa y Business Intelligence."
            )

            st.divider()

            # ======================================================
            # DATASETS
            # ======================================================

            selected_dataset = DatasetPanel.render(
                selected_dataset
            )

            st.divider()

            # ======================================================
            # MÓDULOS
            # ======================================================

            st.subheader("⚙️ Módulos")

            st.checkbox(
                "Análisis Automático",
                value=True,
                disabled=True,
            )

            st.checkbox(
                "Dashboards",
                value=True,
                disabled=True,
            )

            st.checkbox(
                "IA Generativa",
                value=True,
                disabled=True,
            )

            st.checkbox(
                "Business Intelligence",
                value=True,
                disabled=True,
            )

            st.divider()

            # ======================================================
            # VERSIÓN
            # ======================================================

            st.caption("Versión 0.3.1")