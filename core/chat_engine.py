"""
core/chat_engine.py

Motor de conversación de Enterprise AI Data Analyst.

Encapsula la comunicación con el proveedor LLM.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Optional

from config.logging_config import get_logger

from llm.base_llm import BaseLLM

from core.prompt_builder import PromptBuilder

logger = get_logger(__name__)


class ChatEngine:
    """
    Motor encargado de interactuar con
    el proveedor LLM.

    En futuras versiones este módulo
    integrará:

    - Prompt Engineering
    - Memoria
    - RAG
    - Herramientas
    - Agentes IA
    """

    def __init__(
        self,
        llm: BaseLLM,
    ) -> None:
        """
        Inicializa el motor de conversación.
        """

        self.llm = llm

        self.prompt_builder = PromptBuilder()

    def ask(
        self,
        question: str,
        context: Optional[str] = None,
    ) -> str:
        """
        Envía una consulta al LLM.
        """

        logger.info(
            "Construyendo prompt..."
        )

        prompt = self.prompt_builder.build(
            question=question,
            context=context,
        )

        logger.info(
            "Enviando consulta al LLM..."
        )

        response = self.llm.generate(
            prompt=prompt,
        )

        logger.info(
            "Respuesta recibida del LLM."
        )

        return response