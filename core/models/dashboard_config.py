"""
core/models/dashboard_config.py

Modelo de configuración de dashboards.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from dataclasses import dataclass, field

from plotly.graph_objects import Figure


@dataclass(slots=True)
class DashboardConfig:
    """
    Configuración de un dashboard.
    """

    title: str

    description: str

    figures: list[Figure] = field(
        default_factory=list
    )

    theme: str = "plotly"

    responsive: bool = True

    show_filters: bool = True