"""
core/engines/base_chart_engine.py

Interfaz base para motores de gráficos.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import pandas as pd
from plotly.graph_objects import Figure

from core.models.chart_config import ChartConfig


class BaseChartEngine(ABC):
    """
    Interfaz base para motores gráficos.
    """

    @abstractmethod
    def create_figure(
        self,
        dataframe: pd.DataFrame,
        config: ChartConfig,
    ) -> Figure:
        """
        Genera una figura.
        """

        raise NotImplementedError