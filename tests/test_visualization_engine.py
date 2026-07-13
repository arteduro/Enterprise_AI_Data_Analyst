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
    Ejecuta la prueba del motor
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

    charts = engine.auto_visualize(
        dataframe
    )

    print("\n===== VISUALIZATION ENGINE =====\n")

    print("Gráficos recomendados:\n")

    for chart in charts:
        print(f"- {chart}")


if __name__ == "__main__":
    main()