"""
core/response/response_controller.py

Enterprise Response Controller

Controla el tamaño de la respuesta
devuelta por Gemini.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from core.routing.prompt_router import PromptType


class ResponseController:
    """
    Controla la longitud máxima
    de las respuestas.
    """

    LIMITS = {
        PromptType.SHORT: 60,
        PromptType.SUMMARY: 180,
        PromptType.ANALYSIS: 450,
        PromptType.REPORT: 900,
    }


    def max_output_tokens(
        self,
        prompt_type: PromptType,
    ) -> int:
        """
        Devuelve el límite máximo de tokens
        que Gemini puede generar.
        """

        mapping = {
            PromptType.SHORT: 100,
            PromptType.SUMMARY: 350,
            PromptType.ANALYSIS: 6000,
            PromptType.REPORT: 8000,
        }

        return mapping.get(
            prompt_type,
            512,
        )


    def control(
        self,
        response: str,
        prompt_type: PromptType,
    ) -> str:

        if not response:
            return response

        limit = self.LIMITS.get(
            prompt_type,
            400,
        )

        words = response.split()

        if len(words) <= limit:
            return response

        shortened = " ".join(words[:limit])

        return (
            shortened
            + "\n\n..."
            + "\n\n[Respuesta resumida automáticamente por Enterprise AI Router]"
        )