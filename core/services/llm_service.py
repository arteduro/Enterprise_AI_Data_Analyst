"""
core/services/llm_service.py

Servicio de acceso a modelos LLM.

Centraliza toda la comunicación con Gemini.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Optional

from llm.gemini_client import GeminiClient


class LLMService:
    """
    Servicio de acceso a modelos LLM.
    """

    def __init__(self):

        self.client = GeminiClient()

    # =====================================================
    # CONSULTA
    # =====================================================

    def ask(
        self,
        question: str,
        context: Optional[str] = None,
    ) -> str:
        """
        Envía una consulta a Gemini.
        """

        return self.client.generate(
            prompt=question,
            context=context,
        )