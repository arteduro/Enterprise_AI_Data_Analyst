"""
core/models/analysis_result.py

Resultado completo del análisis.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from core.models.dashboard_config import DashboardConfig
from core.profile import DatasetProfile


@dataclass
class AnalysisResult:
    """
    Contiene todo el resultado generado por el motor de análisis.
    """

    # ==========================================
    # DataFrame original
    # ==========================================

    dataframe: pd.DataFrame

    # ==========================================
    # Perfil completo del dataset
    # ==========================================

    profile: DatasetProfile

    # ==========================================
    # Dashboard
    # ==========================================

    dashboard: DashboardConfig

    # ==========================================
    # Informe IA
    # ==========================================

    report: str