"""
tests/test_visualization_engine.py

Prueba del VisualizationEngine.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.engines.visualization_engine import (
    VisualizationEngine,
)


def print_chart(chart: dict, title: str) -> None:
    """
    Imprime la configuración de un gráfico.
    """

    print(f"\n===== {title} =====\n")

    print(f"Disponible: {chart['available']}")
    print(f"Tipo: {chart['type']}")
    print("Columnas:")

    for column in chart["columns"]:
        print(f"- {column}")


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

    charts = engine.auto_visualize(dataframe)

    print("Gráficos recomendados:\n")

    for chart in charts:
        print(f"- {chart}")

    print_chart(
        engine.create_histogram(dataframe),
        "HISTOGRAMA",
    )

    print_chart(
        engine.create_boxplot(dataframe),
        "BOXPLOT",
    )

    print_chart(
        engine.create_correlation(dataframe),
        "CORRELATION",
    )

    print_chart(
        engine.create_bar_chart(dataframe),
        "BAR CHART",
    )


if __name__ == "__main__":
    main()