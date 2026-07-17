"""
ui/report.py

Visualización del reporte generado por IA.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st


class Report:
    """
    Muestra el informe generado por Gemini.
    """

    @staticmethod
    def render(report: str) -> None:

        st.subheader("🧠 Informe Ejecutivo de IA")

        if not report:

            st.info(
                "Todavía no existe un reporte generado."
            )

            return

        with st.container(border=True):

            st.markdown(report)

        st.divider()