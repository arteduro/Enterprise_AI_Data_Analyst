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

from core.services.llm_service import LLMService

# =====================================================
# MEMORIA
# =====================================================

from core.memory import ConversationMemory

# =====================================================
# CONTEXT BUILDER
# =====================================================

from core.context.context_builder import (
    ContextBuilder,
)


class ApplicationService:
    """
    Servicio principal de la aplicación.

    Punto único de acceso para:

    - Enterprise Engine
    - Chat
    - Router Inteligente
    - Gemini
    - Memoria Conversacional
    - Context Builder
    - RAG (futuro)
    - Agentes (futuro)
    """

    def __init__(self):

        self.engine = EnterpriseEngine()

        self.chat = DatasetChat()

        self.router = IntentRouter()

        self.llm = LLMService()

        # ==========================================
        # MEMORIA
        # ==========================================

        self.memory = ConversationMemory()

        # ==========================================
        # CONTEXT BUILDER
        # ==========================================

        self.context_builder = ContextBuilder()

        self.current_dataframe: pd.DataFrame | None = None

        self.current_result: AnalysisResult | None = None

    # =====================================================
    # ANALISIS
    # =====================================================

    def analyze(
        self,
        file_path: str | Path,
    ) -> AnalysisResult:

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

        if self.current_result is None:

            return (
                "Primero debes analizar un dataset."
            )

        # ==========================================
        # MEMORIA
        # ==========================================

        self.memory.add_user_message(question)

        # ==========================================
        # ROUTER
        # ==========================================

        route = self.router.route(question)

        # ==========================================
        # MOTOR INTERNO
        # ==========================================

        if route == Route.INTERNAL:

            answer = self.chat.ask(

                self.current_result.dataframe,

                question,
            )

            self.memory.add_assistant_message(
                answer
            )

            return answer

        # ==========================================
        # GEMINI
        # ==========================================

        if route == Route.GEMINI:

            memory = self.memory.build_context()

            context = self.context_builder.build(

                profile=self.current_result.profile,

                memory=memory,

                question=question,
            )

            answer = self.llm.ask(

                question=question,

                context=context,
            )

            self.memory.add_assistant_message(
                answer
            )

            return answer

        # ==========================================
        # HÍBRIDO
        # ==========================================

        answer = (
            "Modo híbrido aún no implementado."
        )

        self.memory.add_assistant_message(
            answer
        )

        return answer

    # =====================================================
    # UTILIDADES
    # =====================================================

    def has_dataset(self) -> bool:

        return self.current_result is not None

    def dataframe(self) -> pd.DataFrame | None:

        if self.current_result is None:

            return None

        return self.current_result.dataframe

    def analysis_result(self) -> AnalysisResult | None:

        return self.current_result

    # =====================================================
    # MEMORIA
    # =====================================================

    def conversation_history(self):

        return self.memory.messages()

    def clear_memory(self):

        self.memory.clear()

    # =====================================================
    # COMPATIBILIDAD CLI
    # =====================================================

    def generate_dashboard_html(
        self,
        file_path: str | Path,
    ) -> str:

        return self.engine.analyze_file(
            file_path
        )