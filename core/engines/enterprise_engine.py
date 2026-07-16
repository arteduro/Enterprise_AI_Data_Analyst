"""
core/engines/enterprise_engine.py

Motor principal de Enterprise AI Data Analyst.

Orquesta todo el flujo de análisis.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.data_processor import DataProcessor
from core.ai.ai_report_engine import AIReportEngine
from core.engines.visualization_engine import VisualizationEngine
from core.engines.plotly_engine import PlotlyEngine
from core.engines.dashboard_engine import DashboardEngine
from core.models.dashboard_config import DashboardConfig


class EnterpriseEngine:
    """
    Orquestador principal del sistema.
    """

    def __init__(self):

        self.processor = DataProcessor()

        self.ai = AIReportEngine()

        self.visualization = VisualizationEngine()

        self.plotly = PlotlyEngine()

        self.dashboard = DashboardEngine()

    def analyze_dataframe(
        self,
        dataframe: pd.DataFrame,
        output_path: str = "dashboard.html",
    ) -> str:
        """
        Ejecuta el flujo completo de Enterprise AI Data Analyst.
        """

        # ======================================================
        # 1. Analizar Dataset
        # ======================================================

        analysis = self.processor.profile(dataframe)

        # ======================================================
        # 2. Generar Reporte IA
        # ======================================================

        report = self.ai.generate_report(
            analysis.ai_context
        )

        # ======================================================
        # 3. Crear Visualizaciones
        # ======================================================

        figures = [
            self.plotly.create_figure(
                dataframe,
                self.visualization.create_histogram(dataframe),
            ),
            self.plotly.create_figure(
                dataframe,
                self.visualization.create_boxplot(dataframe),
            ),
            self.plotly.create_figure(
                dataframe,
                self.visualization.create_correlation(dataframe),
            ),
            self.plotly.create_figure(
                dataframe,
                self.visualization.create_bar_chart(dataframe),
            ),
        ]

        # ======================================================
        # 4. Construir Dashboard
        # ======================================================

        dashboard = DashboardConfig(
            title="Enterprise AI Data Analyst",
            description="Dashboard generado automáticamente.",
            figures=figures,
            report=report,
        )

        return self.dashboard.save_html(
            dashboard,
            output_path,
        )