"""
core/enterprise_ai.py

Núcleo principal de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Optional

from llm.base_llm import BaseLLM
from llm.llm_factory import LLMFactory

from core.database import DatabaseManager
from core.engines.analysis_engine import AnalysisEngine


class EnterpriseAI:
    """
    Núcleo principal del sistema.

    EnterpriseAI coordina todos los componentes
    principales del proyecto.

    Componentes:

    - AnalysisEngine
    - DatabaseManager
    - LLM
    """

    def __init__(self) -> None:
        """
        Inicializa todos los componentes del sistema.
        """

        # Inteligencia Artificial
        self.llm: BaseLLM = LLMFactory.create()

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
        Envía una consulta al proveedor LLM.
        """

        return self.llm.generate(
            prompt=question,
            context=context,
        )

    def health_check(self) -> bool:
        """
        Comprueba que el proveedor IA responde.
        """

        return self.llm.health_check()