"""
tests/test_recommendation_engine.py

Prueba del RecommendationEngine.

Autor: Edgar Arteaga
"""

from core.profilers.basic_profiler import BasicProfile
from core.profilers.ml_profiler import MLProfile
from core.profilers.quality_profiler import QualityProfile
from core.profilers.recommendation_engine import (
    RecommendationEngine,
)


def main():
    """
    Ejecuta una prueba del motor de recomendaciones.
    """

    basic = BasicProfile(
        rows=500,
        columns=8,
        numeric_columns=5,
        categorical_columns=3,
        datetime_columns=0,
        boolean_columns=1,
        memory_usage_mb=2.5,
        dtypes={
            "edad": "int64",
            "nombre": "object",
        },
    )

    quality = QualityProfile(
        missing_values=12,
        duplicated_rows=4,
        quality_score=92.5,
    )

    ml = MLProfile(
        enough_rows=True,
        possible_target="compró",
        problem_type="Clasificación",
        recommended_models=[
            "Logistic Regression",
            "Random Forest",
            "XGBoost",
        ],
        preprocessing_steps=[
            "Eliminar valores nulos",
            "Codificar variables categóricas",
        ],
    )

    engine = RecommendationEngine()

    recommendations = engine.generate(
        basic=basic,
        quality=quality,
        ml=ml,
    )

    print()

    print("===== RECOMMENDATION ENGINE =====")

    print()

    for recommendation in recommendations:
        print(f"- {recommendation}")

    print()


if __name__ == "__main__":
    main()