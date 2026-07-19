"""
app_streamlit.py

Enterprise AI Data Analyst

Frontend V2

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st

from core.application.session_manager import SessionManager
from core.dataset_selector import DatasetSelector

from ui.header import Header
from ui.sidebar import Sidebar
from ui.main_layout import MainLayout


# ==========================================================
# CONFIGURACIÓN STREAMLIT
# ==========================================================

st.set_page_config(
    page_title="Enterprise AI Data Analyst",
    page_icon="🤖",
    layout="wide",
)

# ==========================================================
# SESSION
# ==========================================================

SessionManager.initialize()

app = SessionManager.app()

def main():
    """
    Punto de entrada principal de la aplicación.
    """

    # ======================================================
    # HEADER
    # ======================================================

    Header.render()

    # ======================================================
    # DATASETS
    # ======================================================

    selector = DatasetSelector()

    datasets = selector.list_datasets()

    if not datasets:

        st.error(
            "No existen datasets disponibles."
        )

        return

    dataset = st.sidebar.selectbox(
        "Seleccione un Dataset",
        datasets,
        format_func=lambda x: x.name,
    )

    Sidebar.render(dataset)

    # ======================================================
    # BOTÓN ANALIZAR
    # ======================================================

    if st.button(
        "🚀 Analizar Dataset",
        use_container_width=True,
    ):

        with st.spinner(
            "Analizando dataset..."
        ):

            result = app.analyze(
                str(dataset)
            )

            SessionManager.set_analysis_result(
                result
            )

        st.success(
            "Dataset analizado correctamente."
        )

        st.rerun()

    # ======================================================
    # MOSTRAR ÚLTIMO ANÁLISIS
    # ======================================================

    result = SessionManager.analysis_result()

    if result is None:

        st.info(
            "Selecciona un dataset y pulsa "
            "'Analizar Dataset'."
        )

        return

    # ======================================================
    # FRONTEND V2
    # ======================================================

    MainLayout.render(
        app=app,
        result=result,
    )


if __name__ == "__main__":
    main()