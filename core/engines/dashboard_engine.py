"""
core/engines/dashboard_engine.py

Motor para generación de dashboards HTML.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

from config.logging_config import get_logger
from core.layouts.dashboard_layout import DashboardLayout
from core.models.dashboard_config import DashboardConfig

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
            dashboard,
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
        Construye el HTML utilizando DashboardLayout.
        """

        logger.info(
            "Construyendo layout del dashboard..."
        )

        return DashboardLayout.build(
            dashboard,
        )