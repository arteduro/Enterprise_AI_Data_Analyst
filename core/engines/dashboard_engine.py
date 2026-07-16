"""
core/engines/dashboard_engine.py

Motor principal del Dashboard.

Autor: Edgar Arteaga
"""

from pathlib import Path

from core.layouts.dashboard_layout import DashboardLayout
from core.models.dashboard_config import DashboardConfig


class DashboardEngine:
    """
    Orquestador principal del Dashboard.
    """

    def save_html(
        self,
        dashboard: DashboardConfig,
        output_path: str,
        report: str = "",
    ) -> str:
        """
        Genera y guarda el Dashboard HTML.
        """

        html = DashboardLayout.build(
            dashboard=dashboard,
            report=report,
        )

        output = Path(output_path)

        output.write_text(
            html,
            encoding="utf-8",
        )

        return str(output.resolve())