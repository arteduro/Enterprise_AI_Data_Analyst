"""
tests/test_ml_profiler.py

Prueba del MLProfiler.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.profilers.ml_profiler import MLProfiler


def main():
    """
    Ejecuta una prueba sencilla del perfilador ML.
    """

    df = pd.DataFrame(
        {
            "edad": [20, 25, 30, 35, 40],
            "salario": [1500, 1800, 2200, 2600, 3000],
            "experiencia": [1, 2, 3, 5, 8],
            "contratado": [
                "Sí",
                "Sí",
                "No",
                "Sí",
                "No",
            ],
        }
    )

    profiler = MLProfiler()

    profile = profiler.analyze(df)

    print()

    print("===== ML PROFILER =====")

    print(f"Suficientes registros: {profile.enough_rows}")

    print(f"Posible target: {profile.possible_target}")

    print(f"Tipo de problema: {profile.problem_type}")

    print()

    print("Modelos recomendados:")

    for model in profile.recommended_models:
        print(f"  - {model}")

    print()

    print("Preprocesamiento recomendado:")

    for step in profile.preprocessing_steps:
        print(f"  - {step}")

    print()


if __name__ == "__main__":
    main()