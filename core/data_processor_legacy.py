"""
core/data_processor.py

Motor de análisis de datasets para Enterprise AI Data Analyst.

Coordina todos los profilers y genera un AnalysisResult.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from config.logging_config import get_logger

from core.analysis import AnalysisResult
from core.exceptions import DatasetError

from core.profilers.basic_profiler import (
    BasicProfiler,
)

from core.profilers.statistics_profiler import (
    StatisticsProfiler,
)

from core.profilers.quality_profiler import (
    QualityProfiler,
)

from core.profilers.ml_profiler import (
    MLProfiler,
)

from core.profilers.recommendation_engine import (
    RecommendationEngine,
)

logger = get_logger(__name__)


# ==========================================================
# Procesador Inteligente
# ==========================================================


class DataProcessor:
    """
    Orquesta todo el proceso de análisis
    de un DataFrame.

    Este módulo coordina los distintos
    profilers del sistema.

    No calcula estadísticas directamente.

    No calcula calidad.

    No calcula recomendaciones.

    Todo eso se delega a los módulos
    especializados.

                