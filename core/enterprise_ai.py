"""
core/enterprise_ai.py

Núcleo principal de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from typing import Optional

from llm.base_llm import BaseLLM
from llm.llm_factory import LLMFactory


class EnterpriseAI:
    """
    Núcleo de Inteligencia Artificial.

    Esta clase abstrae completamente el proveedor
    de IA (Gemini, OpenAI, Claude, Ollama, etc.).

    El resto del proyecto únicamente interactúa
    con EnterpriseAI.
    """

    def __init__(self):

        self.llm: BaseLLM = LLMFactory.create()

    def ask(
        self,
        question: str,
        context: Optional[str] = None
    ) -> str:
        """
        Envía una consulta al modelo LLM.
        """

        return self.llm.generate(
            prompt=question,
            context=context
        )

    def health_check(self) -> bool:
        """
        Comprueba que el proveedor responde.
        """

        return self.llm.health_check()