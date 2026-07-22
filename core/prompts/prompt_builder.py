"""
core/prompts/prompt_builder.py

Enterprise Prompt Builder

Genera prompts optimizados para Gemini.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from core.routing.prompt_router import PromptType
from core.reasoning.reasoning_templates import build_reasoning_prompt


class PromptBuilder:
    """
    Construye prompts optimizados
    para minimizar el consumo de tokens.
    """

    # =====================================================
    # ANALYSIS
    # =====================================================

    def build_analysis_prompt(
        self,
        rows: int,
        cols: int,
        columns: str,
        knowledge: str,
        memory: str,
        question: str,
    ) -> str:

        return f"""
Eres un Senior Enterprise Data Analyst.

DATASET
- Filas: {rows}
- Columnas: {cols}
- Variables: {columns}

KNOWLEDGE
{knowledge}

MEMORIA
{memory}

PREGUNTA
{question}

INSTRUCCIONES

• Usa únicamente el contexto.
• No inventes datos.
• Explica el razonamiento.
• Entrega recomendaciones accionables.
""".strip()

    # =====================================================
    # GENERIC
    # =====================================================

    def build(
        self,
        prompt_type: PromptType,
    ) -> str:

        if prompt_type == PromptType.SHORT:

            return (
                "Responde en máximo tres líneas."
            )

        if prompt_type == PromptType.SUMMARY:

            return (
                "Genera un resumen ejecutivo."
            )

        if prompt_type == PromptType.ANALYSIS:

            return (
                "Realiza un análisis profesional."
            )

        if prompt_type == PromptType.REPORT:

            return (
                "Genera un informe ejecutivo."
            )

        return (
            "Responde como Analista Senior."
        )