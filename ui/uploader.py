"""
ui/uploader.py

Enterprise Dataset Uploader

Responsabilidades
-----------------
- Mostrar datasets disponibles.
- Permitir subir nuevos datasets.
- Activar el dataset seleccionado.
- Mantener el Dataset Demo.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path
import shutil

import streamlit as st

from core.ingestion.dataset_manager import DatasetManager
from core.application.session_manager import SessionManager


class Uploader:
    """
    Componente encargado de gestionar
    la carga y selección de datasets.
    """

    @staticmethod
    def render() -> Path | None:

        manager = SessionManager.dataset_manager()

        st.subheader("📂 Dataset")

        option = st.radio(
            "Seleccione una opción",
            (
                "Usar dataset existente",
                "Subir nuevo dataset",
            ),
        )

        # ----------------------------------------
        # DATASET EXISTENTE
        # ----------------------------------------

        if option == "Usar dataset existente":

            datasets = manager.list_available_datasets()

            if not datasets:

                st.warning(
                    "No existen datasets disponibles."
                )

                return None

            selected = st.selectbox(
                "Dataset",
                datasets,
                format_func=lambda x: x.name,
            )

            manager.activate_dataset(selected)

            return selected

        # ----------------------------------------
        # SUBIR DATASET
        # ----------------------------------------

        uploaded = st.file_uploader(
            "Seleccione un archivo",
            type=[
                "xlsx",
                "xls",
                "csv",
                "json",
                "parquet",
            ],
        )

        if uploaded is None:

            return None

        destination = (
            manager.UPLOADED_FOLDER / uploaded.name
        )

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(destination, "wb") as f:

            shutil.copyfileobj(uploaded, f)

        manager.activate_dataset(destination)

        st.success(
            f"{uploaded.name} cargado correctamente."
        )

        return destination