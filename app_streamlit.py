"""
app_streamlit.py

Interfaz principal de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st

from core.application.application_service import ApplicationService
from core.dataset_selector import DatasetSelector

from ui.sidebar import Sidebar
from ui.header import Header
from ui.metrics import Metrics
from ui.charts import Charts
from ui.report import Report


# ==========================================================
# CACHE DEL ANALISIS COMPLETO
# ==========================================================

@st.cache_data(show_spinner=False)
def cached_analysis(dataset_path: str):
    """
    Ejecuta el análisis completo una sola vez
    para un mismo dataset.
    """

    app = ApplicationService()

    return app.analyze(dataset_path)


# ==========================================================
# CONFIGURACION STREAMLIT
# ==========================================================

st.set_page_config(
    page_title="Enterprise AI Data Analyst",
    page_icon="🤖",
    layout="wide",
)


# ==========================================================
# INTERFAZ PRINCIPAL
# ==========================================================

def main():

    Header.render()

    selector = DatasetSelector()

    datasets = selector.list_datasets()

    if not datasets:

        st.error("No existen datasets disponibles.")

        return

    dataset = st.sidebar.selectbox(
        "Seleccione un Dataset",
        datasets,
        format_func=lambda x: x.name,
    )

    Sidebar.render(dataset)

    st.sidebar.divider()

    analizar = st.sidebar.button(
        "🚀 Analizar Dataset",
        width="stretch",
    )

    if not analizar:
        return

    with st.spinner("Analizando dataset..."):

        result = cached_analysis(str(dataset))

    # =====================================================
    # KPIs
    # =====================================================

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

    st.divider()

    # =====================================================
    # TABS PRINCIPALES
    # =====================================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 Resumen",
            "📈 Visualizaciones",
            "🤖 Informe IA",
            "📋 Datos",
        ]
    )

    # =====================================================
    # RESUMEN
    # =====================================================

    with tab1:

        st.subheader("Resumen del Dataset")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Filas",
                f"{len(result.dataframe):,}"
            )

            st.metric(
                "Columnas",
                len(result.dataframe.columns)
            )

        with col2:

            memoria = (
                result.dataframe.memory_usage(
                    deep=True
                ).sum()
                / 1024
                / 1024
            )

            st.metric(
                "Memoria",
                f"{memoria:.2f} MB"
            )

            st.metric(
                "Valores nulos",
                int(
                    result.dataframe
                    .isna()
                    .sum()
                    .sum()
                )
            )

        st.info(
            "Seleccione la pestaña "
            "**Visualizaciones** "
            "para explorar los gráficos."
        )

    # =====================================================
    # VISUALIZACIONES
    # =====================================================

    with tab2:

        st.subheader("Visualizaciones")

        Charts.render(
            result.dashboard.figures
        )

    # =====================================================
    # INFORME IA
    # =====================================================

    with tab3:

        st.subheader(
            "Reporte Ejecutivo"
        )

        Report.render(
            result.report
        )

    # =====================================================
    # DATOS
    # =====================================================

    with tab4:

        st.subheader(
            "Vista previa del Dataset"
        )

        st.dataframe(
            result.dataframe,
            width="stretch",
            height=650,
        )

    st.success(
        "Análisis completado correctamente."
    )


if __name__ == "__main__":
    main()