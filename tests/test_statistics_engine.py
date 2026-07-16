"""
tests/test_statistics_engine.py

Prueba del StatisticsEngine.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.ai.statistics_engine import StatisticsEngine


def main():

    df = pd.DataFrame(
        {
            "edad": [20, 25, 30, 40],
            "salario": [1200, 1800, 2500, 4000],
            "ventas": [10, 15, 20, 28],
            "ciudad": [
                "Cúcuta",
                "Bogotá",
                "Medellín",
                "Cali",
            ],
        }
    )

    print("\n===== STATISTICS ENGINE =====\n")

    statistics = StatisticsEngine.describe(df)

    for column, values in statistics.items():

        print("\n" + "=" * 50)
        print(column.upper())
        print("=" * 50)

        for key, value in values.items():

            print(f"{key:10}: {value}")

    print("\n")
    print("=" * 50)
    print("MATRIZ DE CORRELACIÓN")
    print("=" * 50)

    correlation = StatisticsEngine.correlation(df)

    for column, values in correlation.items():

        print(f"\n{column}")

        for key, value in values.items():

            print(f"   {key:10}: {value}")


if __name__ == "__main__":
    main()