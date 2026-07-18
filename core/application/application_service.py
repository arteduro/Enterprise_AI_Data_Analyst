"""
core/application/application_service.py

Capa de aplicación de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

from core.engines.enterprise_engine import EnterpriseEngine
from core.models.analysis_result import AnalysisResult


class ApplicationService:
    """
    Servicio principal de la aplicación.
    """

    def __init__(self):

        self.engine = EnterpriseEngine()

    def analyze(
        self,
        file_path: str | Path,
    ) -> AnalysisResult:
        """
        Devuelve el resultado completo del análisis.
        """

        dataframe = self.engine.loader.load(file_path)

        return self.engine.analyze_dataframe(dataframe)

    def generate_dashboard_html(
        self,
        file_path: str | Path,
    ) -> str:
        """
        Compatibilidad con la versión CLI.
        """

        return self.engine.analyze_file(file_path)