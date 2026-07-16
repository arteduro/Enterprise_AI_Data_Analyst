"""
core/components/dashboard_header.py

Header Enterprise del Dashboard.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from core.models.dashboard_config import DashboardConfig


class DashboardHeader:
    """
    Encabezado Enterprise.
    """

    @staticmethod
    def render(
        dashboard: DashboardConfig,
    ) -> str:

        return f"""
<header class="dashboard-header">

    <div class="header-left">

        <div class="logo">

            🤖

        </div>

        <div class="header-text">

            <h1>Enterprise AI Data Analyst</h1>

            <h2>Enterprise Intelligence Platform</h2>

            <p>

                Powered by Gemini • Plotly • Python • AI Analytics

            </p>

        </div>

    </div>

    <div class="header-right">

        <div class="status">

            🟢 ONLINE

        </div>

        <div class="badges">

            <span>📊 {len(dashboard.figures)} Charts</span>

            <span>🧠 AI Ready</span>

            <span>⚡ Gemini</span>

            <span>📅 2026</span>

        </div>

    </div>

</header>
""".strip()