"""
tests/test_dataset_profiler.py

Prueba del DatasetProfiler.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.ai.dataset_profiler import DatasetProfiler


def main():

    df = pd.DataFrame(
        {
            "edad": [20, 25, 30, 40],
            "salario": [1200, 1800, 2500, 4000],
            "ciudad": [
                "Cúcuta",
                "Bogotá",
                "Medellín",
                "Cali",
            ],
        }
    )

    profile = DatasetProfiler.profile(df)

    print("\n===== DATASET PROFILER =====\n")

    print(f"Filas: {profile['rows']}")
    print(f"Columnas: {profile['columns']}")

    print("\nColumnas:")
    print(profile["column_names"])

    print("\nNuméricas:")
    print(profile["numeric_columns"])

    print("\nCategóricas:")
    print(profile["categorical_columns"])

    print("\nValores nulos:")
    print(profile["missing_values"])

    print("\nDuplicados:")
    print(profile["duplicates"])

    print("\nMemoria:")
    print(f"{profile['memory_usage_mb']} MB")


if __name__ == "__main__":
    main()