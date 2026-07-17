"""
ui/metrics.py

Tarjetas KPI para Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st


class Metrics:

    """
    Muestra las métricas principales del análisis.
    """

    @staticmethod
    def render(
        rows: int = 0,
        columns: int = 0,
        numeric_columns: int = 0,
        missing_values: int = 0,
    ) -> None:

        st.subheader("📊 Resumen del Dataset")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="Filas",
                value=f"{rows:,}",
            )

        with col2:
            st.metric(
                label="Columnas",
                value=columns,
            )

        with col3:
            st.metric(
                label="Variables Numéricas",
                value=numeric_columns,
            )

        with col4:
            st.metric(
                label="Valores Nulos",
                value=f"{missing_values:,}",
            )

        st.divider()