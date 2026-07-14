"""
core/engines/dashboard_engine.py

Motor para generación de dashboards HTML.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

from config.logging_config import get_logger
from core.models.dashboard_config import DashboardConfig
from core.themes.dashboard_theme import DashboardTheme

logger = get_logger(__name__)


class DashboardEngine:
    """
    Motor encargado de generar dashboards HTML.
    """

    def save_html(
        self,
        dashboard: DashboardConfig,
        output_path: str,
    ) -> Path:
        """
        Guarda un dashboard HTML.
        """

        logger.info(
            "Generando dashboard HTML..."
        )

        html = self._build_html(
            dashboard
        )

        output = Path(output_path)

        output.write_text(
            html,
            encoding="utf-8",
        )

        logger.info(
            "Dashboard generado correctamente."
        )

        return output

    def _build_html(
        self,
        dashboard: DashboardConfig,
    ) -> str:
        """
        Construye el HTML completo del dashboard.
        """

        logger.info(
            "Construyendo HTML..."
        )

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

<header>

<h1>{dashboard.title}</h1>

<p>{dashboard.description}</p>

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