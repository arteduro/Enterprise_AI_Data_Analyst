"""
core/models/chart_config.py

Modelo de configuración para gráficos de
Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ChartConfig:
    """
    Representa la configuración de un gráfico.

    Este objeto será utilizado por los motores
    de visualización y posteriormente por
    Plotly, Dashboards y Reportes.
    """

    type: str

    available: bool

    columns: list[str] = field(
        default_factory=list
    )

    title: str = ""

    description: str = ""

    engine: str = "plotly"

    interactive: bool = True