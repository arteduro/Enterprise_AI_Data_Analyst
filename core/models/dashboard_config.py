"""
core/models/dashboard_config.py

Modelo de configuración de dashboards.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from dataclasses import dataclass, field

from plotly.graph_objects import Figure

from core.models.ai_report import AIReport


@dataclass(slots=True)
class DashboardConfig:
    """
    Configuración del Dashboard Enterprise.
    """

    title: str

    description: str

    figures: list[Figure] = field(
        default_factory=list
    )

    report: AIReport | None = None

    theme: str = "plotly"

    responsive: bool = True

    show_filters: bool = True