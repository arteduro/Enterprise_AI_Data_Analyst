"""
tests/test_visualization_engine.py

Prueba del VisualizationEngine.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.engines.visualization_engine import (
    VisualizationEngine,
)


def main() -> None:
    """
    Ejecuta las pruebas del motor
    de visualización.
    """

    dataframe = pd.DataFrame(
        {
            "edad": [20, 25, 30, 40, 35],
            "salario": [1500, 2000, 3000, 5000, 4500],
            "ciudad": [
                "Cúcuta",
                "Bogotá",
                "Medellín",
                "Cali",
                "Cúcuta",
            ],
            "contratado": [
                "Sí",
                "Sí",
                "No",
                "Sí",
                "No",
            ],
        }
    )

    engine = VisualizationEngine()

    print("\n===== VISUALIZATION ENGINE =====\n")

    charts = engine.auto_visualize(
        dataframe
    )

    print("Gráficos recomendados:\n")

    for chart in charts:
        print(f"- {chart}")

    histogram = engine.create_histogram(
        dataframe
    )

    print("\n===== HISTOGRAMA =====\n")

    print(f"Disponible: {histogram['available']}")
    print(f"Tipo: {histogram['type']}")
    print("Columnas:")

    for column in histogram["columns"]:
        print(f"- {column}")

    boxplot = engine.create_boxplot(
        dataframe
    )

    print("\n===== BOXPLOT =====\n")

    print(f"Disponible: {boxplot['available']}")
    print(f"Tipo: {boxplot['type']}")
    print("Columnas:")

    for column in boxplot["columns"]:
        print(f"- {column}")


if __name__ == "__main__":
    main()