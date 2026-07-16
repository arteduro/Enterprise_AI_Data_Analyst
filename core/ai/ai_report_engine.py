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
    Genera informes utilizando el contexto producido
    por DataProcessor.
    """

    def __init__(self):

        self.llm = GeminiClient()

    def build_prompt(
        self,
        ai_context: str,
    ) -> str:
        """
        Construye el prompt utilizando el contexto
        generado por DataProcessor.
        """

        return InsightsPrompt.build(ai_context)

    def generate_report(
        self,
        ai_context: str,
    ) -> AIReport:
        """
        Genera el informe utilizando Gemini.
        """

        start = time.perf_counter()

        prompt = self.build_prompt(ai_context)

        report = self.llm.generate(prompt)

        elapsed = time.perf_counter() - start

        return AIReport(
            prompt=prompt,
            report=report,
            model="gemini-2.5-flash",
            execution_time=elapsed,
        )