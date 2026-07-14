"""
tests/test_dashboard_engine.py

Prueba del DashboardEngine.

Autor: Edgar Arteaga
"""

from pathlib import Path

import pandas as pd

from core.engines.dashboard_engine import DashboardEngine
from core.engines.plotly_engine import PlotlyEngine
from core.engines.visualization_engine import VisualizationEngine
from core.models.dashboard_config import DashboardConfig


def main() -> None:
    """
    Ejecuta la prueba del DashboardEngine.
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

    figures = [
        plotly_engine.create_figure(
            dataframe,
            visualization_engine.create_histogram(dataframe),
        ),
        plotly_engine.create_figure(
            dataframe,
            visualization_engine.create_boxplot(dataframe),
        ),
        plotly_engine.create_figure(
            dataframe,
            visualization_engine.create_correlation(dataframe),
        ),
        plotly_engine.create_figure(
            dataframe,
            visualization_engine.create_bar_chart(dataframe),
        ),
    ]

    dashboard = DashboardConfig(
        title="Dashboard de Prueba",
        description="Dashboard generado automáticamente por Enterprise AI Data Analyst.",
        figures=figures,
    )

    output_path = "dashboard.html"

    engine = DashboardEngine()

    result = engine.save_html(
        dashboard,
        output_path,
    )

    print("\n===== DASHBOARD ENGINE =====\n")

    print(f"Archivo generado: {result}")

    print(f"Existe: {Path(result).exists()}")

    print("\nDashboard generado correctamente.")


if __name__ == "__main__":
    main()