"""
ui/uploader.py

Componente encargado de seleccionar datasets.

Permite:

- Subir Excel
- Subir CSV
- Elegir datasets existentes

Autor: Edgar Arteaga
"""

from pathlib import Path
import shutil

import streamlit as st


DATASET_DIR = Path("datasets")


def render() -> Path | None:
    """
    Devuelve el dataset seleccionado.
    """

    st.subheader("📂 Dataset")

    option = st.radio(
        "Seleccione una opción",
        (
            "Usar dataset existente",
            "Subir nuevo dataset",
        ),
    )

    # ---------------------------------------------------------
    # DATASET EXISTENTE
    # ---------------------------------------------------------

    if option == "Usar dataset existente":

        datasets = sorted(DATASET_DIR.glob("*"))

        datasets = [
            d for d in datasets
            if d.suffix.lower()
            in (
                ".xlsx",
                ".xls",
                ".csv",
                ".parquet",
                ".json",
            )
        ]

        if not datasets:

            st.warning(
                "No existen datasets en la carpeta datasets/"
            )

            return None

        selected = st.selectbox(

            "Dataset",

            datasets,

            format_func=lambda x: x.name,

        )

        return selected

    # ---------------------------------------------------------
    # SUBIR ARCHIVO
    # ---------------------------------------------------------

    uploaded = st.file_uploader(

        "Seleccione un archivo",

        type=[
            "xlsx",
            "xls",
            "csv",
            "parquet",
            "json",
        ],

    )

    if uploaded is None:

        return None

    destination = DATASET_DIR / uploaded.name

    with open(destination, "wb") as f:

        shutil.copyfileobj(uploaded, f)

    st.success("Dataset cargado correctamente.")

    return destination