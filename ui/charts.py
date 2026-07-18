"""
ui/charts.py

Renderizado profesional de gráficas Plotly.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st


class Charts:
    """
    Renderiza las figuras Plotly utilizando
    pestañas para mejorar el rendimiento.
    """

    TITULOS = [
        "📊 Histograma",
        "📦 Boxplot",
        "🔥 Correlación",
        "📈 Barras",
    ]

    @staticmethod
    def render(figures: list) -> None:

        st.subheader("📈 Visualizaciones")

        if not figures:

            st.warning(
                "No existen gráficas para mostrar."
            )

            return

        tabs = st.tabs(Charts.TITULOS)

        for tab, figure in zip(tabs, figures):

            with tab:

                st.plotly_chart(
                    figure,
                    width="stretch",
                    key=f"chart_{id(figure)}",
                )

        st.divider()