"""
core/reasoning/enterprise_reasoner.py

Enterprise Reasoning Engine

Decide cómo debe razonar la IA antes de
construir el prompt.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from core.routing.prompt_router import PromptType
from core.reasoning.reasoning_stage import ReasoningStage


class EnterpriseReasoner:
    """
    Motor de razonamiento empresarial.
    """

    def build_pipeline(
        self,
        prompt_type: PromptType,
    ) -> list[ReasoningStage]:

        if prompt_type == PromptType.SHORT:

            return [
                ReasoningStage.OBSERVE,
            ]

        if prompt_type == PromptType.SUMMARY:

            return [
                ReasoningStage.OBSERVE,
                ReasoningStage.PATTERN,
            ]

        if prompt_type == PromptType.ANALYSIS:

            return [
                ReasoningStage.OBSERVE,
                ReasoningStage.PATTERN,
                ReasoningStage.HYPOTHESIS,
                ReasoningStage.VALIDATE,
                ReasoningStage.IMPACT,
                ReasoningStage.RISK,
                ReasoningStage.ACTION,
            ]

        if prompt_type == PromptType.REPORT:

            return [
                ReasoningStage.OBSERVE,
                ReasoningStage.PATTERN,
                ReasoningStage.HYPOTHESIS,
                ReasoningStage.VALIDATE,
                ReasoningStage.IMPACT,
                ReasoningStage.RISK,
                ReasoningStage.ACTION,
                ReasoningStage.KPI,
            ]

        return [
            ReasoningStage.OBSERVE,
        ]
