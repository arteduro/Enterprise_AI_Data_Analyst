"""
ui/charts.py

Renderizado de gráficas Plotly.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st


class Charts:
    """
    Renderiza todas las figuras Plotly
    generadas por EnterpriseEngine.
    """

    @staticmethod
    def render(figures: list) -> None:

        st.subheader("📈 Visualizaciones")

        if not figures:

            st.warning(
                "No existen gráficas para mostrar."
            )

            return

        for figure in figures:

            st.plotly_chart(
                figure,
                use_container_width=True,
            )

        st.divider()