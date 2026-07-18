"""
core/engines/plotly_engine.py

Motor de generación de gráficos con Plotly para
Enterprise AI Data Analyst.

Versión optimizada para alto rendimiento.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

import plotly.graph_objects as go
from plotly.graph_objects import Figure

from config.logging_config import get_logger
from core.engines.base_chart_engine import BaseChartEngine
from core.models.chart_config import ChartConfig

logger = get_logger(__name__)


class PlotlyEngine(BaseChartEngine):
    """
    Motor encargado de generar figuras
    Plotly optimizadas.
    """

    def create_figure(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:

        logger.info(
            "Generando figura Plotly (%s)...",
            config.type,
        )

        if not config.available:
            raise ValueError(
                "La configuración del gráfico no está disponible."
            )

        builders = {
            "histogram": self._create_histogram,
            "boxplot": self._create_boxplot,
            "correlation": self._create_correlation,
            "bar": self._create_bar_chart,
        }

        builder = builders.get(config.type)

        if builder is None:
            raise ValueError(
                f"Tipo de gráfico no soportado: {config.type}"
            )

        figure = builder(
            dataframe,
            config,
        )

        figure.update_layout(
            title=config.title,
            template="plotly_white",
            height=500,
            margin=dict(
                l=30,
                r=30,
                t=60,
                b=30,
            ),
        )

        logger.info(
            "Figura Plotly generada correctamente."
        )

        return figure

    # ==========================================================
    # HISTOGRAMA
    # ==========================================================

    def _create_histogram(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:

        columna = config.columns[0]

        fig = go.Figure()

        fig.add_trace(
            go.Histogram(
                x=dataframe[columna],
                nbinsx=30,
            )
        )

        fig.update_xaxes(title=columna)

        fig.update_yaxes(title="Frecuencia")

        return fig

    # ==========================================================
    # BOXPLOT
    # ==========================================================

    def _create_boxplot(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:

        columna = config.columns[0]

        fig = go.Figure()

        fig.add_trace(

            go.Box(
                y=dataframe[columna],
                name=columna,
                boxpoints=False,
            )

        )

        fig.update_yaxes(title=columna)

        return fig

    # ==========================================================
    # CORRELACION
    # ==========================================================

    def _create_correlation(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:

        corr = dataframe[
            config.columns
        ].corr(
            numeric_only=True
        )

        fig = go.Figure(

            data=go.Heatmap(

                z=corr.values,

                x=corr.columns,

                y=corr.columns,

                text=corr.round(2).values,

                texttemplate="%{text}",

                colorscale="Viridis",

            )

        )

        return fig

    # ==========================================================
    # BARRAS
    # ==========================================================

    def _create_bar_chart(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:

        columna = config.columns[0]

        counts = (
            dataframe[columna]
            .value_counts()
            .head(20)
        )

        fig = go.Figure()

        fig.add_trace(

            go.Bar(

                x=counts.index,

                y=counts.values,

            )

        )

        fig.update_xaxes(title=columna)

        fig.update_yaxes(title="Cantidad")

        return fig