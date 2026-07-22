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
from core.monitoring.token_optimizer import (
    TokenOptimizer,
)

from core.routing.prompt_router import (
    PromptRouter,
)

    TokenOptimizer,
)


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
    • Token Optimizer
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
        # PROMPT ROUTER
        # =====================================

        self.prompt_router = PromptRouter()


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
        # TOKEN OPTIMIZER
        # =====================================

        self.token_optimizer = TokenOptimizer()

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
        # TOKEN OPTIMIZER
        # =====================================

        self.token_optimizer.reset()

        self.token_optimizer.configure(route)

        self.token_optimizer.start()

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

            self.token_optimizer.finish()

            return answer

        # =====================================
        # GEMINI
        # =====================================

        if route == Route.GEMINI:

            memory = self.memory.build_context()

            knowledge = self.knowledge.summary()

            prompt_type = self.prompt_router.route(question)

            context = self.context_builder.build(
                prompt_type=prompt_type,
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

            self.token_optimizer.finish()

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

        self.token_optimizer.finish()

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
    # TOKEN OPTIMIZER
    # =====================================================

    def monitoring(self):

        return self.token_optimizer.metrics()

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
