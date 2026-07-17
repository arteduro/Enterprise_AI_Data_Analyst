"""
ui/sidebar.py

Sidebar principal de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st


class Sidebar:
    """
    Barra lateral principal.
    """

    @staticmethod
    def render(selected_dataset: Path | None = None) -> None:

        with st.sidebar:

            st.title("🤖 IA Empresarial")

            st.divider()

            st.subheader("Proyecto")

            st.write("Enterprise AI Data Analyst")

            st.caption(
                "Plataforma de Analítica, IA Generativa y Business Intelligence."
            )

            st.divider()

            st.subheader("📁 Conjunto de datos")

            if selected_dataset is None:

                st.info("Ningún dataset seleccionado.")

            else:

                st.success(selected_dataset.name)

                st.caption(str(selected_dataset))

            st.divider()

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

            st.caption("Versión 0.2.0")