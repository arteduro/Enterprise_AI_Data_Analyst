"""
core/engines/plotly_engine.py

Motor de generación de gráficos con Plotly para
Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure

from config.logging_config import get_logger
from core.models.chart_config import ChartConfig

logger = get_logger(__name__)


class PlotlyEngine:
    """
    Motor encargado de generar figuras
    de Plotly a partir de un ChartConfig.
    """

    def create_figure(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:
        """
        Genera una figura de Plotly según
        la configuración recibida.
        """

        logger.info(
            "Generando figura Plotly (%s)...",
            config.type,
        )

        if not config.available:
            raise ValueError(
                "La configuración del gráfico no está disponible."
            )

        if config.type == "histogram":
            figure = self._create_histogram(
                dataframe,
                config,
            )

        elif config.type == "boxplot":
            figure = self._create_boxplot(
                dataframe,
                config,
            )

        else:
            raise ValueError(
                f"Tipo de gráfico no soportado: {config.type}"
            )

        figure.update_layout(
            title=config.title,
        )

        logger.info(
            "Figura Plotly generada correctamente."
        )

        return figure

    def _create_histogram(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:
        """
        Genera un histograma.
        """

        return px.histogram(
            dataframe,
            x=config.columns[0],
        )

    def _create_boxplot(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:
        """
        Genera un boxplot.
        """

        return px.box(
            dataframe,
            y=config.columns[0],
        )