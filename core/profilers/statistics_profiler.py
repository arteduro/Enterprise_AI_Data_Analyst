"""
core/profilers/statistics_profiler.py

Perfilador estadístico del dataset.

Genera estadísticas descriptivas de las columnas numéricas.

Autor: Edgar Arteaga
"""

from dataclasses import dataclass, field
from typing import Any

import pandas as pd


# ==========================================================
# Perfil estadístico
# ==========================================================

@dataclass
class StatisticsProfile:
    """
    Contiene las estadísticas descriptivas del dataset.
    """

    statistics: dict[str, Any] = field(
        default_factory=dict
    )


# ==========================================================
# Perfilador estadístico
# ==========================================================

class StatisticsProfiler:
    """
    Genera estadísticas descriptivas de un DataFrame.
    """

    def analyze(
        self,
        df: pd.DataFrame
    ) -> StatisticsProfile:
        """
        Analiza las columnas numéricas del DataFrame.
        """

        numeric = df.select_dtypes(
            include="number"
        )

        if numeric.empty:
            return StatisticsProfile()

        return StatisticsProfile(
            statistics=numeric.describe().to_dict()
        )