"""
core/context/context_builder.py

Enterprise Context Builder

Construye diferentes niveles de contexto
para minimizar el consumo de tokens.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.routing.prompt_router import PromptType
from core.prompts.prompt_builder import PromptBuilder


class ContextBuilder:
    """
    Construye el contexto enviado al LLM
    dependiendo del tipo de consulta.
    """

    def __init__(self):

        self.prompt_builder = PromptBuilder()


    # =====================================================
    # SHORT
    # =====================================================

    def build_short_context(
        self,
        dataframe: pd.DataFrame,
        question: str,
    ) -> str:

        rows, cols = dataframe.shape

        return f"""
DATASET

Filas: {rows}
Columnas: {cols}

Pregunta:

{question}

Responde únicamente la pregunta.
Sé breve.
""".strip()

    # =====================================================
    # SUMMARY
    # =====================================================

    def build_summary_context(
        self,
        dataframe: pd.DataFrame,
        knowledge: str,
        question: str,
    ) -> str:

        rows, cols = dataframe.shape

        columns = ", ".join(dataframe.columns)

        return f"""
DATASET

Filas: {rows}

Columnas: {cols}

Variables:

{columns}

Knowledge Base

{knowledge}

Pregunta

{question}

Responde con un resumen ejecutivo.
""".strip()

    # =====================================================
    # ANALYSIS
    # =====================================================

    def build_analysis_context(
        self,
        dataframe: pd.DataFrame,
        memory: str,
        knowledge: str,
        question: str,
    ) -> str:

        rows, cols = dataframe.shape

        columns = ", ".join(dataframe.columns)

        return f"""
=========================
ENTERPRISE AI ANALYSIS
=========================

DATASET

Filas:
{rows}

Columnas:
{cols}

Variables:

{columns}

----------------------------

KNOWLEDGE BASE

{knowledge}

----------------------------

MEMORIA

{memory}

----------------------------

PREGUNTA

{question}

----------------------------

INSTRUCCIONES

Analiza profundamente.

No inventes datos.

Entrega conclusiones y recomendaciones.
""".strip()

    # =====================================================
    # REPORT
    # =====================================================

    def build_report_context(
        self,
        dataframe: pd.DataFrame,
        memory: str,
        knowledge: str,
        question: str,
    ) -> str:

        context = self.build_analysis_context(
            dataframe,
            memory,
            knowledge,
            question,
        )

        return (
            context
            + "\n\nGenera un informe ejecutivo completo."
        )

    # =====================================================
    # ROUTER
    # =====================================================

    def build(
        self,
        prompt_type: PromptType,
        dataframe: pd.DataFrame,
        memory: str,
        knowledge: str,
        question: str,
    ) -> str:

        if prompt_type == PromptType.SHORT:

            return self.build_short_context(
                dataframe,
                question,
            )

        if prompt_type == PromptType.SUMMARY:

            return self.build_summary_context(
                dataframe,
                knowledge,
                question,
            )

        if prompt_type == PromptType.REPORT:

            return self.build_report_context(
                dataframe,
                memory,
                knowledge,
                question,
            )

        return self.build_analysis_context(
            dataframe,
            memory,
            knowledge,
            question,
        )