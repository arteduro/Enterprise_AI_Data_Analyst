"""
core/ai/ai_report_engine.py

Motor encargado de generar informes mediante IA.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import time

from core.models.ai_report import AIReport
from llm.gemini_client import GeminiClient
from prompts.insights_prompt import InsightsPrompt


class AIReportEngine:
    """
    Orquesta la generación de reportes mediante IA.
    """

    def __init__(self):

        self.llm = GeminiClient()

    def build_prompt(
        self,
        ai_context: str,
    ) -> str:
        """
        Construye el prompt que será enviado al LLM.
        """

        return InsightsPrompt.build(ai_context)

    def generate_report(
        self,
        ai_context: str,
    ) -> AIReport:
        """
        Genera un informe utilizando Gemini.

        Si Gemini no está disponible,
        devuelve un informe de respaldo.
        """

        start = time.perf_counter()

        prompt = self.build_prompt(ai_context)

        try:

            report = self.llm.generate(prompt)

            model = "gemini-2.5-flash"

        except Exception as error:

            report = f"""
# Informe no disponible

No fue posible generar el análisis mediante Gemini.

## Motivo

{error}

## Estado del sistema

- El dataset fue cargado correctamente.
- El análisis estadístico fue completado.
- Las visualizaciones fueron generadas.
- El dashboard puede construirse normalmente.

Intente nuevamente cuando el servicio de IA esté disponible.
""".strip()

            model = "fallback"

        elapsed = time.perf_counter() - start

        return AIReport(
            prompt=prompt,
            report=report,
            model=model,
            execution_time=elapsed,
        )