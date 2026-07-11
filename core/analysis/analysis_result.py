"""
core/analysis/analysis_result.py

Resultado completo del análisis de un dataset.

Agrupa todos los perfiles generados por los módulos
de profiling.

Autor: Edgar Arteaga
"""

from dataclasses import dataclass, field

from core.profilers.basic_profiler import BasicProfile
from core.profilers.ml_profiler import MLProfile
from core.profilers.quality_profiler import QualityProfile
from core.profilers.statistics_profiler import (
    StatisticsProfile,
)


@dataclass
class AnalysisResult:
    """
    Contiene el resultado completo del análisis.
    """

    basic: BasicProfile

    statistics: StatisticsProfile

    quality: QualityProfile

    ml: MLProfile

    recommendations: list[str] = field(
        default_factory=list
    )

    summary: str = ""

    ai_context: str = ""