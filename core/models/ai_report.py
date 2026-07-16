"""
core/models/ai_report.py

Modelo que representa un reporte generado por IA.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class AIReport:
    """
    Representa el resultado generado por un modelo LLM.
    """

    prompt: str

    report: str

    model: str

    execution_time: float

    created_at: datetime = field(
        default_factory=datetime.now
    )