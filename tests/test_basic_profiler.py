"""
tests/test_basic_profiler.py

Prueba del BasicProfiler.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.profilers.basic_profiler import BasicProfiler


def main():
    """
    Ejecuta una prueba sencilla del perfilador básico.
    """

    df = pd.DataFrame(
        {
            "edad": [20, 25, 30],
            "nombre": ["Ana", "Luis", "Carlos"],
            "activo": [True, False, True],
        }
    )

    profiler = BasicProfiler()

    profile = profiler.analyze(df)

    print()

    print("===== BASIC PROFILER =====")

    print(f"Filas: {profile.rows}")

    print(f"Columnas: {profile.columns}")

    print(f"Numéricas: {profile.numeric_columns}")

    print(f"Categóricas: {profile.categorical_columns}")

    print(f"Booleanas: {profile.boolean_columns}")

    print(f"Memoria (MB): {profile.memory_usage_mb}")

    print()

    print("Tipos de datos:")

    for column, dtype in profile.dtypes.items():
        print(f"  {column}: {dtype}")


if __name__ == "__main__":
    main()