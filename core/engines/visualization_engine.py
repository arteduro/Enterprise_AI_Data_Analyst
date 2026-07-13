"""
core/engines/visualization_engine.py

Motor de visualización de Enterprise AI Data Analyst.

Se encarga de recomendar las visualizaciones más
adecuadas para un DataFrame.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from config.logging_config import get_logger

logger = get_logger(__name__)


class VisualizationEngine:
    """
    Motor encargado de recomendar
    visualizaciones para un dataset.

    En futuras versiones generará:

    - Histogramas
    - Boxplots
    - Heatmaps
    - Scatter plots
    - Dashboards
    - Reportes visuales
    """

    def auto_visualize(
        self,
        dataframe: pd.DataFrame,
    ) -> list[str]:
        """
        Recomienda visualizaciones para
        un DataFrame.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Dataset a analizar.

        Returns
        -------
        list[str]
            Lista de gráficos recomendados.
        """

        logger.info(
            "Analizando visualizaciones recomendadas..."
        )

        charts: list[str] = []

        numeric_columns = dataframe.select_dtypes(
            include="number"
        ).columns

        categorical_columns = dataframe.select_dtypes(
            exclude="number"
        ).columns

        if len(numeric_columns) > 0:
            charts.append("histogram")
            charts.append("boxplot")

        if len(numeric_columns) > 1:
            charts.append("correlation")

        if len(categorical_columns) > 0:
            charts.append("bar")

        logger.info(
            "Visualizaciones recomendadas correctamente."
        )

        return charts

    def create_histogram(
        self,
        dataframe: pd.DataFrame,
    ) -> dict:
        """
        Genera la configuración de un histograma.

        En esta primera versión no crea la imagen,
        únicamente devuelve la información necesaria
        para construir el gráfico.
        """

        logger.info(
            "Generando configuración del histograma..."
        )

        numeric_columns = list(
            dataframe.select_dtypes(
                include="number"
            ).columns
        )

        if not numeric_columns:
            logger.warning(
                "No existen variables numéricas."
            )

            return {
                "type": "histogram",
                "available": False,
                "columns": [],
            }

        logger.info(
            "Configuración del histograma generada."
        )

        return {
            "type": "histogram",
            "available": True,
            "columns": numeric_columns,
        }