"""
core/models/analysis_result.py

Resultado completo del análisis.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from core.models.dashboard_config import DashboardConfig


@dataclass
class AnalysisResult:
    """
    Contiene todo el resultado generado por el motor de análisis.
    """

    dataframe: pd.DataFrame

    dashboard: DashboardConfig

    report: str