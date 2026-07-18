"""
core/cache/streamlit_cache.py

Administrador centralizado del caché de Streamlit.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import streamlit as st


class StreamlitCache:
    """
    Gestiona todos los decoradores de caché.

    Centralizar el caché aquí permitirá
    cambiar posteriormente a Redis,
    DiskCache o Azure Cache sin modificar
    el resto del proyecto.
    """

    @staticmethod
    @st.cache_data(show_spinner=False)
    def load_dataframe(loader, file_path):
        """
        Cachea la carga del dataset.
        """
        return loader.load(file_path)

    @staticmethod
    @st.cache_data(show_spinner=False)
    def profile_dataframe(processor, dataframe):
        """
        Cachea el análisis estadístico.
        """
        return processor.profile(dataframe)

    @staticmethod
    @st.cache_resource(show_spinner=False)
    def build_figure(
        plotly_engine,
        dataframe,
        config,
    ):
        """
        Cachea una figura Plotly.
        """
        return plotly_engine.create_figure(
            dataframe,
            config,
        )

    @staticmethod
    @st.cache_data(show_spinner=False)
    def generate_ai_report(
        ai_engine,
        ai_context,
    ):
        """
        Cachea el informe generado por IA.

        Si se vuelve a analizar el mismo dataset,
        Streamlit reutilizará el informe sin volver
        a consultar el proveedor LLM.
        """
        return ai_engine.generate_report(
            ai_context,
        )