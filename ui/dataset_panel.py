"""
ui/dataset_panel.py

Enterprise Dataset Panel

Responsabilidades
-----------------
- Mostrar el estado del dataset activo.
- Integrar el Enterprise Uploader.
- Mostrar información del dataset seleccionado.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from ui.uploader import Uploader


class DatasetPanel:
    """
    Panel lateral para la administración
    de datasets empresariales.
    """

    @staticmethod
    def render(
        selected_dataset: Path | None = None,
    ) -> Path | None:

        st.subheader("📂 Gestión de Datasets")

        st.caption(
            "Seleccione un dataset existente o cargue uno nuevo."
        )

        st.divider()

        # -----------------------------------------
        # Enterprise Uploader
        # -----------------------------------------

        dataset = Uploader.render()

        if dataset is not None:

            selected_dataset = dataset

        st.divider()

        # -----------------------------------------
        # Dataset activo
        # -----------------------------------------

        st.markdown("### 📌 Dataset activo")

        if selected_dataset is None:

            st.info(
                "No hay ningún dataset seleccionado."
            )

        else:

            st.success(selected_dataset.name)

            st.caption(str(selected_dataset))

        return selected_dataset