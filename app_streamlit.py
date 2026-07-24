"""
app_streamlit.py

Enterprise AI Data Analyst

Frontend principal

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st

from core.application.session_manager import SessionManager
from core.ingestion.dataset_manager import DatasetManager

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

dataset_manager = SessionManager.dataset_manager()


def main():
    """
    Punto de entrada principal.
    """

    # ======================================================
    # HEADER
    # ======================================================

    Header.render()

    # ======================================================
    # SIDEBAR
    # ======================================================

    Sidebar.render(
        dataset_manager.get_active_dataset()
    )

    # ======================================================
    # DATASET ACTIVO
    # ======================================================

    dataset = dataset_manager.get_active_dataset()

    if not dataset.exists():

        st.error(
            "No existe un dataset activo."
        )

        return

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
    # RESULTADO
    # ======================================================

    result = SessionManager.analysis_result()

    if result is None:

        st.info(
            "Seleccione un dataset y pulse "
            "'Analizar Dataset'."
        )

        return

    # ======================================================
    # MAIN LAYOUT
    # ======================================================

    MainLayout.render(
        app=app,
        result=result,
    )


if __name__ == "__main__":
    main()