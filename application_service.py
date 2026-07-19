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

# =====================================================
# ROUTER
# =====================================================

from core.routing.intent_router import (
    IntentRouter,
    Route,
)

# =====================================================
# LLM
# =====================================================

from core.services.llm_service import (
    LLMService,
)


class ApplicationService:
    """
    Servicio principal de la plataforma.

    Punto único de acceso para:

    - Enterprise Engine
    - Chat IA
    - Router Inteligente
    - Gemini
    - Memoria (futuro)
    - RAG (futuro)
    - Agentes (futuro)
    """

    def __init__(self):

        # ==========================================
        # Motor principal
        # ==========================================

        self.engine = EnterpriseEngine()

        # ==========================================
        # Chat interno
        # ==========================================

        self.chat = DatasetChat()

        # ==========================================
        # Router Inteligente
        # ==========================================

        self.router = IntentRouter()

        # ==========================================
        # Servicio LLM
        # ==========================================

        self.llm = LLMService()

        # ==========================================
        # Estado actual
        # ==========================================

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
        Analiza completamente un dataset.
        """

        dataframe = self.engine.loader.load(
            file_path
        )

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
        Permite conversar con el dataset utilizando
        el Router Inteligente.
        """

        if self.current_dataframe is None:

            return (
                "Primero debes analizar un dataset."
            )

        # ==============================================
        # DECIDIR QUIÉN RESPONDE
        # ==============================================

        route = self.router.route(question)

        # ==============================================
        # MOTOR INTERNO
        # ==============================================

        if route == Route.INTERNAL:

            return self.chat.ask(
                self.current_dataframe,
                question,
            )

        # ==============================================
        # GEMINI
        # ==============================================

        if route == Route.GEMINI:

            # Contexto inicial del dataset.
            # Más adelante este contexto será reemplazado
            # por RAG + memoria.

            context = (
                f"Columnas:\n"
                f"{list(self.current_dataframe.columns)}\n\n"
                f"Número de filas: "
                f"{len(self.current_dataframe)}\n\n"
                f"Primeras filas:\n"
                f"{self.current_dataframe.head(10).to_markdown(index=False)}"
            )

            return self.llm.ask(
                question=question,
                context=context,
            )

        # ==============================================
        # HÍBRIDO
        # ==============================================

        return (
            "Modo híbrido aún no implementado."
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