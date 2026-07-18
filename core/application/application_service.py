"""
core/application/application_service.py

Capa de aplicación de Enterprise AI Data Analyst.

Coordina todos los servicios de la plataforma.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from core.chat.dataset_chat import DatasetChat
from core.engines.enterprise_engine import EnterpriseEngine
from core.models.analysis_result import AnalysisResult


class ApplicationService:
    """
    Servicio principal de la aplicación.

    Este será el punto único de acceso para:

    - Enterprise Engine
    - Chat
    - Memoria (futuro)
    - RAG (futuro)
    - Agentes (futuro)
    """

    def __init__(self):

        self.engine = EnterpriseEngine()

        self.chat = DatasetChat()

        self.current_dataframe: pd.DataFrame | None = None

        self.current_result: AnalysisResult | None = None

    # =====================================================
    # ANALISIS
    # =====================================================

    def analyze(
        self,
        file_path: str | Path,
    ) -> AnalysisResult:
        """
        Analiza un dataset completo.
        """

        dataframe = self.engine.loader.load(file_path)

        result = self.engine.analyze_dataframe(
            dataframe
        )

        self.current_dataframe = dataframe

        self.current_result = result

        return result

    # =====================================================
    # CHAT
    # =====================================================

    def ask(
        self,
        question: str,
    ) -> str:
        """
        Permite conversar con el dataset
        actualmente cargado.
        """

        if self.current_dataframe is None:

            return (
                "Primero debes analizar un dataset."
            )

        return self.chat.ask(
            self.current_dataframe,
            question,
        )

    # =====================================================
    # UTILIDADES
    # =====================================================

    def has_dataset(self) -> bool:
        """
        Indica si existe un dataset cargado.
        """

        return self.current_dataframe is not None

    def dataframe(self) -> pd.DataFrame | None:
        """
        Devuelve el DataFrame actual.
        """

        return self.current_dataframe

    def analysis_result(self) -> AnalysisResult | None:
        """
        Devuelve el último análisis.
        """

        return self.current_result

    # =====================================================
    # COMPATIBILIDAD CLI
    # =====================================================

    def generate_dashboard_html(
        self,
        file_path: str | Path,
    ) -> str:
        """
        Compatibilidad con la versión CLI.
        """

        return self.engine.analyze_file(
            file_path
        )