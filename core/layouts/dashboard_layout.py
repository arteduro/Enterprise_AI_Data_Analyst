"""
core/layouts/dashboard_layout.py

Layout HTML del Dashboard Enterprise.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from core.models.dashboard_config import DashboardConfig
from core.themes.dashboard_theme import DashboardTheme


class DashboardLayout:
    """
    Construye el HTML completo del dashboard.
    """

    @staticmethod
    def build(
        dashboard: DashboardConfig,
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

<title>{dashboard.title}</title>

<style>

{css}

</style>

</head>

<body>

<div class="container">

<header class="dashboard-header">

<div class="header-info">

<h1>🤖 Enterprise AI Data Analyst</h1>

<p>{dashboard.description}</p>

</div>

<div class="header-status">

<div>📊 {len(dashboard.figures)} gráficos</div>

<div>🧠 IA Ready</div>

<div>📅 2026</div>

<div class="online">🟢 ONLINE</div>

</div>

</header>

<section class="dashboard-grid">

{figures_html}

</section>

<footer>

Enterprise AI Data Analyst © 2026

</footer>

</div>

</body>

</html>
""".strip()