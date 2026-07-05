"""
core/data_processor.py

Motor de análisis de datasets para Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from dataclasses import dataclass, field
from typing import Any

import pandas as pd

from config.logging_config import get_logger
from core.exceptions import DatasetError

logger = get_logger(__name__)


# ==========================================================
# Perfil del Dataset
# ==========================================================

@dataclass
class DatasetProfile:
    """
    Contiene toda la información obtenida del análisis
    de un dataset.
    """

    rows: int = 0
    columns: int = 0

    numeric_columns: int = 0
    categorical_columns: int = 0
    datetime_columns: int = 0

    missing_values: int = 0
    duplicated_rows: int = 0

    memory_usage_mb: float = 0.0

    quality_score: float = 0.0

    dtypes: dict = field(default_factory=dict)

    statistics: dict = field(default_factory=dict)

    recommendations: list[str] = field(default_factory=list)

    summary: str = ""

    ai_context: str = ""


# ==========================================================
# Procesador Inteligente
# ==========================================================

class DataProcessor:
    """
    Analiza un DataFrame y genera un perfil completo.

    Este módulo será utilizado por:

    - Gemini
    - Dashboard
    - AutoML
    - Reportes
    - RAG
    - Agentes IA
    """

    def validate(self, df: pd.DataFrame) -> None:
        """
        Valida que el DataFrame sea correcto.
        """

        if df is None:
            raise DatasetError("El DataFrame es None.")

        if df.empty:
            raise DatasetError("El DataFrame está vacío.")

        if len(df.columns) == 0:
            raise DatasetError("El DataFrame no contiene columnas.")

    def profile(self, df: pd.DataFrame) -> DatasetProfile:
        """
        Genera un perfil completo del dataset.
        """

        self.validate(df)

        logger.info("Analizando dataset...")

        profile = DatasetProfile()

        profile.rows = len(df)

        profile.columns = len(df.columns)

        profile.numeric_columns = len(
            df.select_dtypes(include="number").columns
        )

        profile.categorical_columns = len(
            df.select_dtypes(include="object").columns
        )

        profile.datetime_columns = len(
            df.select_dtypes(include="datetime").columns
        )

        profile.missing_values = int(
            df.isna().sum().sum()
        )

        profile.duplicated_rows = int(
            df.duplicated().sum()
        )

        profile.memory_usage_mb = round(
            df.memory_usage(deep=True).sum() / 1024 / 1024,
            2
        )

        profile.dtypes = {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        }

        profile.statistics = self.statistics(df)

        profile.quality_score = self.quality_score(profile)

        profile.recommendations = self.generate_recommendations(profile)

        profile.summary = self.generate_summary(profile)

        profile.ai_context = self.generate_ai_context(profile)

        logger.info("Perfil generado correctamente.")

        return profile

    def statistics(self, df: pd.DataFrame) -> dict[str, Any]:
        """
        Genera estadísticas para columnas numéricas.
        """

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return {}

        return numeric.describe().to_dict()

    def quality_score(self, profile: DatasetProfile) -> float:
        """
        Calcula un puntaje de calidad entre 0 y 100.
        """

        score = 100.0

        score -= profile.missing_values * 0.05

        score -= profile.duplicated_rows * 0.5

        return max(round(score, 2), 0)

    def generate_recommendations(
        self,
        profile: DatasetProfile
    ) -> list[str]:
        """
        Genera recomendaciones automáticas.
        """

        recommendations = []

        if profile.missing_values > 0:
            recommendations.append(
                "Existen valores nulos. Se recomienda imputarlos o eliminarlos."
            )

        if profile.duplicated_rows > 0:
            recommendations.append(
                "Existen filas duplicadas. Se recomienda eliminarlas."
            )

        if profile.quality_score < 80:
            recommendations.append(
                "La calidad del dataset es baja."
            )

        if not recommendations:
            recommendations.append(
                "El dataset presenta una buena calidad."
            )

        return recommendations

    def generate_summary(
        self,
        profile: DatasetProfile
    ) -> str:
        """
        Genera un resumen ejecutivo.
        """

        return (
            f"Dataset con {profile.rows:,} registros, "
            f"{profile.columns} columnas y "
            f"una calidad estimada del "
            f"{profile.quality_score:.2f}%."
        )

    def generate_ai_context(
        self,
        profile: DatasetProfile
    ) -> str:
        """
        Genera el contexto que será enviado al LLM.
        """

        return f"""
DATASET PROFILE

Filas: {profile.rows}

Columnas: {profile.columns}

Variables numéricas: {profile.numeric_columns}

Variables categóricas: {profile.categorical_columns}

Variables fecha: {profile.datetime_columns}

Valores nulos: {profile.missing_values}

Duplicados: {profile.duplicated_rows}

Uso de memoria: {profile.memory_usage_mb} MB

Calidad: {profile.quality_score:.2f} %

Resumen:

{profile.summary}
""".strip()