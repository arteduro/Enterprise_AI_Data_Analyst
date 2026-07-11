"""
core/data_processor.py

Motor de análisis de datasets para
Enterprise AI Data Analyst.

Coordina todos los profilers y genera
un AnalysisResult.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from config.logging_config import get_logger

from core.analysis import AnalysisResult
from core.exceptions import DatasetError

from core.profilers.basic_profiler import BasicProfiler
from core.profilers.statistics_profiler import StatisticsProfiler
from core.profilers.quality_profiler import QualityProfiler
from core.profilers.ml_profiler import MLProfiler
from core.profilers.recommendation_engine import RecommendationEngine


logger = get_logger(__name__)


# ==========================================================
# Procesador de datos
# ==========================================================


class DataProcessor:
    """
    Orquesta el análisis completo de un DataFrame.

    Coordina todos los profilers del sistema y
    devuelve un AnalysisResult.
    """

    def __init__(self) -> None:
        """
        Inicializa todos los módulos de análisis.
        """

        self.basic_profiler = BasicProfiler()

        self.statistics_profiler = StatisticsProfiler()

        self.quality_profiler = QualityProfiler()

        self.ml_profiler = MLProfiler()

        self.recommendation_engine = RecommendationEngine()

    def validate(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Valida el DataFrame antes del análisis.
        """

        if df is None:
            raise DatasetError(
                "El DataFrame es None."
            )

        if df.empty:
            raise DatasetError(
                "El DataFrame está vacío."
            )

        if len(df.columns) == 0:
            raise DatasetError(
                "El DataFrame no contiene columnas."
            )

    def profile(
        self,
        df: pd.DataFrame,
    ) -> AnalysisResult:
        """
        Ejecuta el análisis completo del DataFrame.
        """

        self.validate(df)

        logger.info(
            "Analizando dataset..."
        )

        basic = self.basic_profiler.analyze(df)

        statistics = self.statistics_profiler.analyze(df)

        quality = self.quality_profiler.analyze(df)

        ml = self.ml_profiler.analyze(df)

        recommendations = (
            self.recommendation_engine.generate(
                basic,
                quality,
                ml,
            )
        )

        summary = self._generate_summary(
            basic,
            quality,
        )

        ai_context = self._generate_ai_context(
            basic,
            quality,
            ml,
            recommendations,
            summary,
        )

        result = AnalysisResult(
            basic=basic,
            statistics=statistics,
            quality=quality,
            ml=ml,
            recommendations=recommendations,
            summary=summary,
            ai_context=ai_context,
        )

        logger.info(
            "Análisis completado correctamente."
        )

        return result

    def _generate_summary(
        self,
        basic,
        quality,
    ) -> str:
        """
        Genera un resumen ejecutivo del análisis.
        """

        return (
            f"Dataset con {basic.rows:,} registros, "
            f"{basic.columns} columnas y "
            f"una calidad estimada del "
            f"{quality.quality_score:.2f}%."
        )
        """
        Genera un resumen ejecutivo del análisis.
        """

        return (
            f"Dataset con {basic.rows:,} registros, "
            f"{basic.columns} columnas y "
            f"una calidad estimada del "
            f"{quality.quality_score:.2f}%."
        )

    def _generate_ai_context(
        self,
        basic,
        quality,
        ml,
        recommendations,
        summary,
    ) -> str:
        """
        Genera el contexto que será enviado al LLM.
        """

        recommendations_text = "\n".join(
            f"- {item}"
            for item in recommendations
        )

        return f"""
DATASET PROFILE

Filas: {basic.rows}

Columnas: {basic.columns}

Variables numéricas: {basic.numeric_columns}

Variables categóricas: {basic.categorical_columns}

Variables fecha: {basic.datetime_columns}

Variables booleanas: {basic.boolean_columns}

Uso de memoria: {basic.memory_usage_mb} MB

Valores nulos: {quality.missing_values}

Duplicados: {quality.duplicated_rows}

Calidad: {quality.quality_score:.2f} %

Posible variable objetivo:
{ml.possible_target}

Tipo de problema:
{ml.problem_type}

Modelos recomendados:
{", ".join(ml.recommended_models)}

Resumen:
{summary}

Recomendaciones:

{recommendations_text}
""".strip()