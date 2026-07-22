"""
core/reasoning/reasoning_result.py

Enterprise Reasoning Result

Autor: Edgar Arteaga
"""

from dataclasses import dataclass

from core.reasoning.reasoning_stage import ReasoningStage


@dataclass
class ReasoningResult:

    pipeline: list[ReasoningStage]

    reasoning_prompt: str

    thinking_depth: str

    complexity: str

    requires_validation: bool

    requires_kpis: bool
