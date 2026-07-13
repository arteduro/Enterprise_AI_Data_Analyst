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
        """

        return self._build_chart(
            dataframe=dataframe,
            chart_type="histogram",
        )

    def create_boxplot(
        self,
        dataframe: pd.DataFrame,
    ) -> dict:
        """
        Genera la configuración de un boxplot.
        """

        return self._build_chart(
            dataframe=dataframe,
            chart_type="boxplot",
        )

    def create_correlation(
        self,
        dataframe: pd.DataFrame,
    ) -> dict:
        """
        Genera la configuración de una
        matriz de correlación.
        """

        return self._build_chart(
            dataframe=dataframe,
            chart_type="correlation",
        )

    def create_bar_chart(
        self,
        dataframe: pd.DataFrame,
    ) -> dict:
        """
        Genera la configuración de un
        gráfico de barras.
        """

        logger.info(
            "Generando configuración de bar..."
        )

        categorical_columns = list(
            dataframe.select_dtypes(
                exclude="number"
            ).columns
        )

        if not categorical_columns:
            logger.warning(
                "No existen variables categóricas."
            )

            return {
                "type": "bar",
                "available": False,
                "columns": [],
            }

        logger.info(
            "Configuración de bar generada."
        )

        return {
            "type": "bar",
            "available": True,
            "columns": categorical_columns,
        }

    def _build_chart(
        self,
        dataframe: pd.DataFrame,
        chart_type: str,
    ) -> dict:
        """
        Construye la configuración base
        para gráficos numéricos.
        """

        logger.info(
            f"Generando configuración de {chart_type}..."
        )

        numeric_columns = list(
            dataframe.select_dtypes(
                include="number"
            ).columns
        )

        if chart_type == "correlation":
            if len(numeric_columns) < 2:
                logger.warning(
                    "Se requieren al menos dos variables numéricas."
                )

                return {
                    "type": chart_type,
                    "available": False,
                    "columns": [],
                }

        elif not numeric_columns:
            logger.warning(
                "No existen variables numéricas."
            )

            return {
                "type": chart_type,
                "available": False,
                "columns": [],
            }

        logger.info(
            f"Configuración de {chart_type} generada."
        )

        return {
            "type": chart_type,
            "available": True,
            "columns": numeric_columns,
        }