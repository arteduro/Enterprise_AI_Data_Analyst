"""
core/profilers/recommendation_engine.py

Motor de recomendaciones para Enterprise AI Data Analyst.

Genera recomendaciones inteligentes a partir
de los perfiles calculados del dataset.

Autor: Edgar Arteaga
"""

from core.profilers.basic_profiler import BasicProfile
from core.profilers.ml_profiler import MLProfile
from core.profilers.quality_profiler import QualityProfile


# ==========================================================
# Motor de recomendaciones
# ==========================================================

class RecommendationEngine:
    """
    Genera recomendaciones automáticas para el dataset.
    """

    def generate(
        self,
        basic: BasicProfile,
        quality: QualityProfile,
        ml: MLProfile,
    ) -> list[str]:
        """
        Genera recomendaciones basadas en los perfiles.
        """

        recommendations: list[str] = []

        if quality.missing_values > 0:
            recommendations.append(
                "Existen valores nulos. Se recomienda imputarlos o eliminarlos."
            )

        if quality.duplicated_rows > 0:
            recommendations.append(
                "Existen filas duplicadas. Se recomienda eliminarlas."
            )

        if quality.quality_score < 80:
            recommendations.append(
                "La calidad del dataset es baja."
            )

        if not ml.enough_rows:
            recommendations.append(
                "El dataset tiene pocos registros para Machine Learning."
            )

        recommendations.append(
            f"Posible variable objetivo: {ml.possible_target}."
        )

        recommendations.append(
            f"Tipo de problema detectado: {ml.problem_type}."
        )

        recommendations.append(
            "Modelos recomendados: "
            + ", ".join(ml.recommended_models)
            + "."
        )

        if basic.categorical_columns > 0:
            recommendations.append(
                "Se recomienda codificar las variables categóricas."
            )

        if basic.numeric_columns > 0:
            recommendations.append(
                "Se recomienda escalar las variables numéricas."
            )

        return recommendations