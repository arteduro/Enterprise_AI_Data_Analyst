"""
core/components/dashboard_kpis.py

Tarjetas KPI del Dashboard Enterprise.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from core.models.dashboard_config import DashboardConfig


class DashboardKPIs:
    """
    Renderiza los KPIs superiores del dashboard.
    """

    @staticmethod
    def render(
        dashboard: DashboardConfig,
    ) -> str:

        total_charts = len(dashboard.figures)

        return f"""
<section class="kpi-grid">

    <div class="kpi-card">

        <div class="kpi-value">
            {total_charts}
        </div>

        <div class="kpi-label">
            Gráficos
        </div>

    </div>

    <div class="kpi-card">

        <div class="kpi-value">
            IA
        </div>

        <div class="kpi-label">
            Enterprise Ready
        </div>

    </div>

    <div class="kpi-card">

        <div class="kpi-value">
            100%
        </div>

        <div class="kpi-label">
            Calidad
        </div>

    </div>

    <div class="kpi-card">

        <div class="kpi-value">
            ✔
        </div>

        <div class="kpi-label">
            Dashboard Activo
        </div>

    </div>

</section>
""".strip()