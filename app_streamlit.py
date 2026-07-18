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
    Ejecuta el análisis completo y almacena el resultado
    para evitar reprocesar el mismo dataset.
    """

    app = ApplicationService()

    result = app.analyze(dataset_path)

    return result


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

    if st.button(
        "🚀 Analizar Dataset",
        width="stretch",
    ):

        with st.spinner("Analizando dataset..."):

            result = cached_analysis(str(dataset))

        # ----------------------------------------

        app = ApplicationService()

        app._last_dataframe = result.dataframe

        # ----------------------------------------

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📊 Resumen",
                "📈 Visualizaciones",
                "🤖 Informe IA",
                "📄 Datos",
            ]
        )

        # ==================================================
        # TAB RESUMEN
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
        # TAB GRAFICOS
        # ==================================================

        with tab2:

            Charts.render(
                result.dashboard.figures
            )

        # ==================================================
        # TAB INFORME IA
        # ==================================================

        with tab3:

            Report.render(
                result.report
            )

            st.divider()

            st.subheader("💬 Chat con el Dataset")

            question = st.text_input(
                "Escribe una pregunta sobre el dataset",
                placeholder="Ejemplo: ¿Cuántas filas tiene el dataset?"
            )

            if st.button(
                "Preguntar",
                key="chat_button",
            ):

                if question.strip():

                    answer = app.ask(question)

                    st.markdown("### 🤖 Respuesta")

                    st.write(answer)

                else:

                    st.warning(
                        "Escribe una pregunta."
                    )

        # ==================================================
        # TAB DATOS
        # ==================================================

        with tab4:

            st.dataframe(
                result.dataframe,
                width="stretch",
            )


if __name__ == "__main__":
    main()