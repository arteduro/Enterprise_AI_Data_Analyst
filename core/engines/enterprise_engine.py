"""
core/engines/enterprise_engine.py

Motor principal de Enterprise AI Data Analyst.

Orquesta todo el flujo de análisis.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from core.ai.ai_report_engine import AIReportEngine
from core.data_processor import DataProcessor
from core.document_loader import DocumentLoader
from core.engines.plotly_engine import PlotlyEngine
from core.engines.visualization_engine import VisualizationEngine
from core.layouts.dashboard_layout import DashboardLayout
from core.models.analysis_result import AnalysisResult
from core.models.dashboard_config import DashboardConfig


class EnterpriseEngine:
    """
    Orquestador principal del sistema.
    """

    def __init__(self) -> None:

        self.loader = DocumentLoader()

        self.processor = DataProcessor()

        self.ai = AIReportEngine()

        self.visualization = VisualizationEngine()

        self.plotly = PlotlyEngine()

    def analyze_file(
        self,
        file_path: str | Path,
    ) -> str:
        """
        Analiza un archivo y genera el dashboard HTML.
        """

        dataframe = self.loader.load(file_path)

        result = self.analyze_dataframe(dataframe)

        html = DashboardLayout.build(
            result.dashboard,
            result.report,
        )

        output = Path("dashboard.html")

        output.write_text(
            html,
            encoding="utf-8",
        )

        return str(output.resolve())

    def analyze_dataframe(
        self,
        dataframe: pd.DataFrame,
    ) -> AnalysisResult:
        """
        Analiza un DataFrame completo.
        """

        analysis = self.processor.profile(dataframe)

        report = self.ai.generate_report(
            analysis.ai_context,
        )

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

        dashboard = DashboardConfig(
            title="Enterprise AI Data Analyst",
            description="Dashboard generado automáticamente",
            figures=figures,
            report=report.report,
        )

        return AnalysisResult(
            dataframe=dataframe,
            dashboard=dashboard,
            report=report.report,
        )