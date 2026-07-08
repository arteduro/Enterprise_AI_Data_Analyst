"""
core/profilers/quality_profiler.py

Perfilador de calidad del dataset.

Evalúa la calidad de los datos y detecta
problemas comunes.

Autor: Edgar Arteaga
"""

from dataclasses import dataclass

import pandas as pd


# ==========================================================
# Perfil de calidad
# ==========================================================

@dataclass
class QualityProfile:
    """
    Contiene las métricas de calidad del dataset.
    """

    missing_values: int

    duplicated_rows: int

    quality_score: float


# ==========================================================
# Perfilador de calidad
# ==========================================================

class QualityProfiler:
    """
    Evalúa la calidad general del DataFrame.
    """

    def analyze(
        self,
        df: pd.DataFrame
    ) -> QualityProfile:
        """
        Analiza la calidad del dataset.
        """

        missing_values = int(
            df.isna().sum().sum()
        )

        duplicated_rows = int(
            df.duplicated().sum()
        )

        score = 100.0

        score -= missing_values * 0.05

        score -= duplicated_rows * 0.5

        score = max(
            round(score, 2),
            0
        )

        return QualityProfile(
            missing_values=missing_values,
            duplicated_rows=duplicated_rows,
            quality_score=score,
        )