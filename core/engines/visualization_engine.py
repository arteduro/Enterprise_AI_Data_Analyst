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