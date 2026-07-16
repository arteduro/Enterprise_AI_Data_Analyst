"""
core/layouts/dashboard_layout.py

Layout HTML del Dashboard Enterprise.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from core.components.ai_report_card import AIReportCard
from core.components.dashboard_header import DashboardHeader
from core.components.dashboard_kpis import DashboardKPIs
from core.components.dashboard_sidebar import DashboardSidebar
from core.models.dashboard_config import DashboardConfig
from core.themes.dashboard_theme import DashboardTheme


class DashboardLayout:
    """
    Construye el HTML completo del Dashboard Enterprise.
    """

    @staticmethod
    def build(
        dashboard: DashboardConfig,
        report: str = "",
    ) -> str:

        css = DashboardTheme.css()

        cards = []

        include_plotly = True

        for figure in dashboard.figures:

            figure_html = figure.to_html(
                full_html=False,
                include_plotlyjs="cdn"
                if include_plotly
                else False,
            )

            include_plotly = False

            cards.append(
                f"""
<div class="card">

{figure_html}

</div>
""".strip()
            )

        figures_html = "\n".join(cards)

        return f"""
<!DOCTYPE html>

<html lang="es">

<head>

<meta charset="utf-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>{dashboard.title}</title>

<style>

{css}

</style>

</head>

<body>

<div class="app-layout">

    {DashboardSidebar.render()}

    <main class="main-content">

        {DashboardHeader.render(dashboard)}

        {DashboardKPIs.render(dashboard)}

        <section class="dashboard-grid">

            {figures_html}

        </section>

        {AIReportCard.render(report)}

        <footer>

            Enterprise AI Data Analyst © 2026

        </footer>

    </main>

</div>

</body>

</html>
""".strip()