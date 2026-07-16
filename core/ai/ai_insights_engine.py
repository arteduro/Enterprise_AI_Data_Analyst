"""
core/ai/ai_insights_engine.py

Motor de preparación de insights para IA.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.ai.dataset_profiler import DatasetProfiler
from core.ai.statistics_engine import StatisticsEngine


class AIInsightsEngine:
    """
    Construye el contexto que será enviado al LLM.
    """

    @staticmethod
    def build_context(
        df: pd.DataFrame,
    ) -> dict:

        profile = DatasetProfiler.profile(df)

        statistics = StatisticsEngine.describe(df)

        correlations = StatisticsEngine.correlation(df)

        return {

            "profile": profile,

            "statistics": statistics,

            "correlations": correlations,

        }