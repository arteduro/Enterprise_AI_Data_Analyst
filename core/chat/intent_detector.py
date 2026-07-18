"""
core/chat/intent_detector.py

Detector de intención para el Chat Empresarial.

Determina si una pregunta puede responderse
con Pandas o requiere un LLM.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from enum import Enum


class Intent(Enum):
    """
    Tipos de intención soportados.
    """

    PANDAS = "pandas"

    LLM = "llm"


class IntentDetector:
    """
    Detector simple basado en palabras clave.

    En versiones futuras podrá sustituirse
    por un clasificador basado en IA.
    """

    PANDAS_KEYWORDS = [

        "fila",
        "filas",

        "columna",
        "columnas",

        "nulo",
        "nulos",

        "vacío",
        "vacios",
        "vacíos",

        "promedio",
        "media",

        "máximo",
        "maximo",

        "mínimo",
        "minimo",

        "suma",

        "conteo",

        "cuántos",
        "cuantas",
        "cuántas",

        "total",

        "lista",

        "valor",

        "duplicado",
        "duplicados",

        "tipo de dato",
        "tipos de dato",

        "variables",

        "estadística",
        "estadisticas",
        "estadísticas",
    ]

    @classmethod
    def detect(
        cls,
        question: str,
    ) -> Intent:
        """
        Devuelve el tipo de intención.
        """

        question = question.lower()

        for keyword in cls.PANDAS_KEYWORDS:

            if keyword in question:

                return Intent.PANDAS

        return Intent.LLM