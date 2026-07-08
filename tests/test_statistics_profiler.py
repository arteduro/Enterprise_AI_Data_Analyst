"""
tests/test_statistics_profiler.py

Prueba del StatisticsProfiler.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.profilers.statistics_profiler import (
    StatisticsProfiler,
)


def main():
    """
    Ejecuta una prueba sencilla del perfilador estadístico.
    """

    df = pd.DataFrame(
        {
            "edad": [20, 25, 30, 35, 40],
            "salario": [1500, 1800, 2200, 2600, 3000],
            "nombre": [
                "Ana",
                "Luis",
                "Carlos",
                "Marta",
                "Pedro",
            ],
        }
    )

    profiler = StatisticsProfiler()

    profile = profiler.analyze(df)

    print()

    print("===== STATISTICS PROFILER =====")

    print()

    for column, stats in profile.statistics.items():

        print(f"Columna: {column}")

        for key, value in stats.items():

            print(f"  {key}: {value}")

        print()


if __name__ == "__main__":
    main()