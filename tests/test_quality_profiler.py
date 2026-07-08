"""
tests/test_quality_profiler.py

Prueba del QualityProfiler.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.profilers.quality_profiler import (
    QualityProfiler,
)


def main():
    """
    Ejecuta una prueba sencilla del perfilador de calidad.
    """

    df = pd.DataFrame(
        {
            "edad": [20, 25, None, 30, 20],
            "nombre": [
                "Ana",
                "Luis",
                "Carlos",
                "Pedro",
                "Ana",
            ],
        }
    )

    # Agregamos una fila duplicada
    df = pd.concat(
        [df, df.iloc[[0]]],
        ignore_index=True
    )

    profiler = QualityProfiler()

    profile = profiler.analyze(df)

    print()

    print("===== QUALITY PROFILER =====")

    print(f"Valores nulos: {profile.missing_values}")

    print(f"Filas duplicadas: {profile.duplicated_rows}")

    print(f"Calidad: {profile.quality_score}%")

    print()


if __name__ == "__main__":
    main()