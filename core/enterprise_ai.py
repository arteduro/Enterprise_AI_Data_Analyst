"""
core/enterprise_ai.py

Núcleo principal de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Optional

from llm.base_llm import BaseLLM
from llm.llm_factory import LLMFactory

from core.chat_engine import ChatEngine
from core.database import DatabaseManager
from core.engines.analysis_engine import AnalysisEngine


class EnterpriseAI:
    """
    Núcleo principal del sistema.

    EnterpriseAI coordina todos los componentes
    principales del proyecto.

    Componentes:

    - AnalysisEngine
    - ChatEngine
    - DatabaseManager
    - LLM
    """

    def __init__(self) -> None:
        """
        Inicializa todos los componentes del sistema.
        """

        # Inteligencia Artificial
        self.llm: BaseLLM = LLMFactory.create()

        # Motor de conversación
        self.chat_engine = ChatEngine(
            self.llm
        )

        # Motor de análisis
        self.analysis_engine = AnalysisEngine()

        # Persistencia
        self.database = DatabaseManager()

    def ask(
        self,
        question: str,
        context: Optional[str] = None,
    ) -> str:
        """
        Envía una consulta al motor de conversación.
        """

        return self.chat_engine.ask(
            question=question,
            context=context,
        )

    def ask_file(
        self,
        file_path: str,
        question: str,
    ) -> str:
        """
        Analiza un archivo y utiliza el resultado
        para responder una pregunta.
        """

        analysis = self.analysis_engine.analyze_file(
            file_path
        )

        return self.chat_engine.ask(
            question=question,
            context=analysis.ai_context,
        )

    def health_check(self) -> bool:
        """
        Comprueba que el proveedor IA responde.
        """

        return self.llm.health_check()