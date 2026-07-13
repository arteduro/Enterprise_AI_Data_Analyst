"""
tests/test_plotly_engine.py

Prueba del PlotlyEngine.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.engines.plotly_engine import PlotlyEngine
from core.engines.visualization_engine import VisualizationEngine


def main() -> None:
    """
    Ejecuta la prueba del motor Plotly.
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
        }
    )

    visualization_engine = VisualizationEngine()
    plotly_engine = PlotlyEngine()

    chart = visualization_engine.create_histogram(
        dataframe
    )

    figure = plotly_engine.create_figure(
        dataframe,
        chart,
    )

    print("\n===== PLOTLY ENGINE =====\n")

    print(f"Tipo de figura: {type(figure).__name__}")
    print(f"Título: {figure.layout.title.text}")

    print("\nNúmero de trazas:")
    print(len(figure.data))

    print("\nGráfico generado correctamente.")


if __name__ == "__main__":
    main()