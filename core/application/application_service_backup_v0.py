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
from core.context.context_builder import ContextBuilder
from core.engines.enterprise_engine import EnterpriseEngine
from core.knowledge import KnowledgeBase
from core.memory import ConversationMemory
from core.models.analysis_result import AnalysisResult
from core.routing.intent_router import (
    IntentRouter,
    Route,
)
from core.services.llm_service import LLMService


class ApplicationService:
    """
    Servicio principal de la aplicación.

    Coordina:

    • Enterprise Engine
    • Dataset Chat
    • Router Inteligente
    • Gemini
    • Memoria Conversacional
    • Context Builder
    • Knowledge Base
    """

    def __init__(self):

        # =====================================
        # MOTOR ANALÍTICO
        # =====================================

        self.engine = EnterpriseEngine()

        # =====================================
        # CHAT LOCAL
        # =====================================

        self.chat = DatasetChat()

        # =====================================
        # ROUTER IA
        # =====================================

        self.router = IntentRouter()

        # =====================================
        # SERVICIO LLM
        # =====================================

        self.llm = LLMService()

        # =====================================
        # MEMORIA CONVERSACIONAL
        # =====================================

        self.memory = ConversationMemory()

        # =====================================
        # CONTEXT BUILDER
        # =====================================

        self.context_builder = ContextBuilder()

        # =====================================
        # KNOWLEDGE BASE
        # =====================================

        self.knowledge = KnowledgeBase()

        # =====================================
        # DATASET ACTUAL
        # =====================================

        self.current_dataframe: pd.DataFrame | None = None

        self.current_result: AnalysisResult | None = None

    # =====================================================
    # ANALIZAR DATASET
    # =====================================================

    def analyze(
        self,
        file_path: str | Path,
    ) -> AnalysisResult:

        dataframe = self.engine.loader.load(file_path)

        result = self.engine.analyze_dataframe(
            dataframe
        )

        self.current_dataframe = dataframe

        self.current_result = result

        # =====================================
        # GENERAR KNOWLEDGE BASE
        # =====================================

        self.knowledge.build(dataframe)

        return result

    # =====================================================
    # CHAT
    # =====================================================

    def ask(
        self,
        question: str,
    ) -> str:

        if self.current_dataframe is None:

            return (
                "Primero debes analizar un dataset."
            )

        # =====================================
        # MEMORIA
        # =====================================

        self.memory.add_user_message(question)

        # =====================================
        # ROUTER
        # =====================================

        route = self.router.route(question)

        # =====================================
        # MOTOR LOCAL
        # =====================================

        if route == Route.INTERNAL:

            answer = self.chat.ask(
                self.current_dataframe,
                question,
            )

            self.memory.add_assistant_message(
                answer
            )

            return answer

        # =====================================
        # GEMINI
        # =====================================

        if route == Route.GEMINI:

            memory = self.memory.build_context()

            knowledge = self.knowledge.summary()

            context = self.context_builder.build(
                dataframe=self.current_dataframe,
                memory=memory,
                knowledge=knowledge,
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

        # =====================================
        # HÍBRIDO
        # =====================================

        answer = (
            "Modo híbrido aún no implementado."
        )

        self.memory.add_assistant_message(
            answer
        )

        return answer

    # =====================================================
    # DATASET
    # =====================================================

    def has_dataset(self) -> bool:

        return self.current_dataframe is not None

    def dataframe(self):

        return self.current_dataframe

    def analysis_result(self):

        return self.current_result

    # =====================================================
    # MEMORIA
    # =====================================================

    def conversation_history(self):

        return self.memory.messages()

    def clear_memory(self):

        self.memory.clear()

    # =====================================================
    # KNOWLEDGE BASE
    # =====================================================

    def knowledge_summary(self):

        return self.knowledge.summary()

    def knowledge_data(self):

        return self.knowledge.get()

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