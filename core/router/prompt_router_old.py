"""
core/router/prompt_router.py

Enterprise Prompt Router

Decide el nivel de detalle que debe tener
la respuesta enviada al LLM.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from enum import Enum


class PromptType(str, Enum):

    SHORT = "short"

    SUMMARY = "summary"

    ANALYSIS = "analysis"

    REPORT = "report"


class PromptRouter:
    """
    Clasifica el tipo de prompt que debe
    enviarse al LLM.
    """

    SHORT_KEYWORDS = {
        "cuántas",
        "cuantos",
        "cantidad",
        "total",
        "nombre",
        "nombres",
        "listar",
        "lista",
        "columnas",
        "filas",
    }

    REPORT_KEYWORDS = {
        "informe",
        "reporte",
        "dashboard",
        "análisis completo",
        "analisis completo",
        "diagnóstico",
        "diagnostico",
    }

    ANALYSIS_KEYWORDS = {
        "analiza",
        "analizar",
        "explica",
        "comparar",
        "compara",
        "tendencia",
        "correlación",
        "correlacion",
        "predicción",
        "prediccion",
    }

    def route(
        self,
        question: str,
    ) -> PromptType:

        q = question.lower()

        # ---------------------------------
        # REPORT
        # ---------------------------------

        if any(k in q for k in self.REPORT_KEYWORDS):

            return PromptType.REPORT

        # ---------------------------------
        # ANALYSIS
        # ---------------------------------

        if any(k in q for k in self.ANALYSIS_KEYWORDS):

            return PromptType.ANALYSIS

        # ---------------------------------
        # SHORT
        # ---------------------------------

        if any(k in q for k in self.SHORT_KEYWORDS):

            return PromptType.SHORT

        # ---------------------------------
        # DEFAULT
        # ---------------------------------

        return PromptType.SUMMARY