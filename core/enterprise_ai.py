"""
core/enterprise_ai.py

Núcleo principal de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from typing import Optional

from llm.base_llm import BaseLLM
from llm.llm_factory import LLMFactory

from core.document_loader import DocumentLoader
from core.data_processor import DataProcessor
from core.database import DatabaseManager


class EnterpriseAI:
    """
    Núcleo principal del sistema.

    EnterpriseAI coordina todos los componentes:

    - DocumentLoader
    - DataProcessor
    - DatabaseManager
    - LLM
    """

    def __init__(self):

        # Inteligencia Artificial
        self.llm: BaseLLM = LLMFactory.create()

        # Procesamiento de datos
        self.loader = DocumentLoader()

        self.processor = DataProcessor()

        # Persistencia
        self.database = DatabaseManager()

    def ask(
        self,
        question: str,
        context: Optional[str] = None
    ) -> str:
        """
        Envía una consulta al LLM.
        """

        return self.llm.generate(
            prompt=question,
            context=context
        )

    def health_check(self) -> bool:
        """
        Comprueba que el proveedor IA responde.
        """

        return self.llm.health_check()