"""
ui/main_layout.py

Layout principal de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st

from ui.metrics import Metrics
from ui.charts import Charts
from ui.report import Report
from ui.chat import Chat


class MainLayout:
    """
    Layout principal de la aplicación.
    """

    @staticmethod
    def render(
        app,
        result,
    ):

        # ==================================================
        # TABS PRINCIPALES
        # ==================================================

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "📊 Resumen",
                "📈 Visualizaciones",
                "🤖 Informe IA",
                "💬 Chat IA",
                "📄 Datos",
            ]
        )

        # ==================================================
        # TAB 1 - RESUMEN
        # ==================================================

        with tab1:

            Metrics.render(
                rows=len(result.dataframe),
                columns=len(result.dataframe.columns),
                numeric_columns=len(
                    result.dataframe.select_dtypes("number").columns
                ),
                missing_values=int(
                    result.dataframe.isna().sum().sum()
                ),
            )

            st.success(
                "Análisis completado correctamente."
            )

        # ==================================================
        # TAB 2 - VISUALIZACIONES
        # ==================================================

        with tab2:

            Charts.render(
                result.dashboard.figures
            )

        # ==================================================
        # TAB 3 - INFORME IA
        # ==================================================

        with tab3:

            Report.render(
                result.report
            )

        # ==================================================
        # TAB 4 - CHAT IA
        # ==================================================

        with tab4:

            Chat.render(app)

        # ==================================================
        # TAB 5 - DATAFRAME
        # ==================================================

        with tab5:

            st.dataframe(
                result.dataframe,
                use_container_width=True,
            )