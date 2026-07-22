"""
core/reasoning/reasoning_stage.py

Enterprise AI Data Analyst

Define las etapas cognitivas que seguirá
el Enterprise Reasoning Engine.

Autor: Edgar Arteaga
"""

from enum import Enum


class ReasoningStage(str, Enum):
    """
    Pipeline de razonamiento empresarial.
    """

    OBSERVE = "observe"

    PATTERN = "pattern"

    HYPOTHESIS = "hypothesis"

    VALIDATE = "validate"

    IMPACT = "impact"

    RISK = "risk"

    ACTION = "action"

    KPI = "kpi"
