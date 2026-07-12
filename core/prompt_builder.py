"""
core/prompt_builder.py

Constructor de prompts para Enterprise AI Data Analyst.

Se encarga de construir el prompt que será enviado
al proveedor LLM.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Optional


class PromptBuilder:
    """
    Construye prompts para los distintos
    casos de uso del sistema.

    En futuras versiones soportará:

    - Chat general
    - Análisis de datasets
    - SQL
    - Dashboard
    - AutoML
    - RAG
    - Agentes IA
    """

    def build(
        self,
        question: str,
        context: Optional[str] = None,
    ) -> str:
        """
        Construye el prompt que será enviado
        al proveedor LLM.
        """

        if context:

            return f"""
Eres Enterprise AI Data Analyst.

Analiza cuidadosamente el siguiente contexto antes de responder.

========================
CONTEXTO
========================

{context}

========================
PREGUNTA
========================

{question}

Responde de forma clara, técnica y profesional.
""".strip()

        return f"""
Eres Enterprise AI Data Analyst.

Pregunta:

{question}

Responde de forma clara, técnica y profesional.
""".strip()