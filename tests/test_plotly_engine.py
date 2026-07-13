"""
tests/test_plotly_engine.py

Prueba del PlotlyEngine.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.engines.plotly_engine import PlotlyEngine
from core.engines.visualization_engine import VisualizationEngine


def print_figure(title: str, figure) -> None:
    """
    Imprime información de una figura.
    """

    print(f"\n===== {title} =====\n")

    print(f"Tipo: {type(figure).__name__}")
    print(f"Título: {figure.layout.title.text}")
    print(f"Número de trazas: {len(figure.data)}")


def main() -> None:
    """
    Ejecuta la prueba del PlotlyEngine.
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

    visualization_engine = VisualizationEngine()
    plotly_engine = PlotlyEngine()

    histogram = plotly_engine.create_figure(
        dataframe,
        visualization_engine.create_histogram(dataframe),
    )

    boxplot = plotly_engine.create_figure(
        dataframe,
        visualization_engine.create_boxplot(dataframe),
    )

    correlation = plotly_engine.create_figure(
        dataframe,
        visualization_engine.create_correlation(dataframe),
    )

    bar_chart = plotly_engine.create_figure(
        dataframe,
        visualization_engine.create_bar_chart(dataframe),
    )

    print("\n===== PLOTLY ENGINE =====")

    print_figure(
        "HISTOGRAMA",
        histogram,
    )

    print_figure(
        "BOXPLOT",
        boxplot,
    )

    print_figure(
        "CORRELATION",
        correlation,
    )

    print_figure(
        "BAR CHART",
        bar_chart,
    )

    print("\nTodas las figuras fueron generadas correctamente.")


if __name__ == "__main__":
    main()