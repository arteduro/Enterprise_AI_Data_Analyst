"""
core/profilers/ml_profiler.py

Perfilador de Machine Learning.

Analiza un dataset y genera recomendaciones
para tareas de aprendizaje automático.

Autor: Edgar Arteaga
"""

from dataclasses import dataclass, field

import pandas as pd


# ==========================================================
# Perfil de Machine Learning
# ==========================================================

@dataclass
class MLProfile:
    """
    Contiene información útil para Machine Learning.
    """

    enough_rows: bool

    possible_target: str

    problem_type: str

    recommended_models: list[str] = field(
        default_factory=list
    )

    preprocessing_steps: list[str] = field(
        default_factory=list
    )


# ==========================================================
# Perfilador ML
# ==========================================================

class MLProfiler:
    """
    Analiza un DataFrame desde la perspectiva
    de Machine Learning.
    """

    def analyze(
        self,
        df: pd.DataFrame
    ) -> MLProfile:
        """
        Genera un perfil para tareas de Machine Learning.
        """

        enough_rows = len(df) >= 100

        target = df.columns[-1]

        if pd.api.types.is_numeric_dtype(df[target]):
            problem_type = "Regresión"

            recommended_models = [
                "Linear Regression",
                "Random Forest Regressor",
                "XGBoost Regressor",
            ]
        else:
            problem_type = "Clasificación"

            recommended_models = [
                "Logistic Regression",
                "Random Forest",
                "XGBoost",
            ]

        preprocessing_steps = [
            "Eliminar valores nulos",
            "Eliminar filas duplicadas",
            "Codificar variables categóricas",
            "Escalar variables numéricas",
        ]

        return MLProfile(
            enough_rows=enough_rows,
            possible_target=target,
            problem_type=problem_type,
            recommended_models=recommended_models,
            preprocessing_steps=preprocessing_steps,
        )