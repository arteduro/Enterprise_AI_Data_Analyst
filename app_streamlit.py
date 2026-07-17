"""
app_streamlit.py

Interfaz principal Streamlit.

Enterprise AI Data Analyst

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

from core.application.application_service import ApplicationService
from core.dataset_selector import DatasetSelector

from ui.sidebar import Sidebar
from ui.header import Header
from ui.metrics import Metrics
from ui.charts import Charts
from ui.report import Report


st.set_page_config(
    page_title="Enterprise AI Data Analyst",
    page_icon="🤖",
    layout="wide",
)


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
        use_container_width=True,
    ):

        with st.spinner("Analizando información..."):

            app = ApplicationService()

            dashboard = app.engine.analyze_file(dataset)

            dataframe = pd.read_excel(dataset)

        Metrics.render(
            rows=len(dataframe),
            columns=len(dataframe.columns),
            numeric_columns=len(
                dataframe.select_dtypes("number").columns
            ),
            missing_values=int(
                dataframe.isna().sum().sum()
            ),
        )

        st.subheader("Vista previa")

        st.dataframe(
            dataframe.head(20),
            use_container_width=True,
        )

        st.divider()

        Charts.render(dashboard.figures)

        Report.render(
            dashboard.report,
        )

        st.success("Proceso finalizado correctamente.")


if __name__ == "__main__":
    main()