"""
core/routing/intent_router.py

Router inteligente de consultas.

Este módulo decide si una pregunta debe responderse
mediante el motor interno del proyecto o utilizando
un modelo LLM (Gemini).

Autor: Edgar Arteaga
"""

from __future__ import annotations

from enum import Enum


class Route(Enum):
    """
    Destinos posibles para una consulta.
    """

    INTERNAL = "internal"
    GEMINI = "gemini"
    HYBRID = "hybrid"


class IntentRouter:
    """
    Router principal del sistema.
    """

    def __init__(self):

        self.internal_keywords = [

            "promedio",
            "media",
            "máximo",
            "maximo",
            "mínimo",
            "minimo",
            "filas",
            "columnas",
            "nulos",
            "variables",
            "conteo",
            "total",
            "suma",

        ]

    # =====================================================
    # ROUTING
    # =====================================================

    def route(
        self,
        question: str,
    ) -> Route:
        """
        Decide qué motor debe responder.
        """

        question = question.lower()

        for keyword in self.internal_keywords:

            if keyword in question:

                return Route.INTERNAL

        return Route.GEMINI