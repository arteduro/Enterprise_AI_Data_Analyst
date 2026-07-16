"""
core/components/dashboard_sidebar.py

Componente Sidebar del Dashboard Enterprise.

Autor: Edgar Arteaga
"""

from __future__ import annotations


class DashboardSidebar:
    """
    Construye el menú lateral del Dashboard Enterprise.
    """

    @staticmethod
    def render() -> str:
        """
        Devuelve el HTML del Sidebar.
        """

        return """
<aside class="sidebar">

    <div class="sidebar-logo">

        🤖

    </div>

    <h2>Enterprise AI</h2>

    <p>Analytics Platform</p>

    <nav class="sidebar-menu">

        <a href="#">📊 Dashboard</a>

        <a href="#">🧠 AI Insights</a>

        <a href="#">📈 Visualizaciones</a>

        <a href="#">⚠ Alertas</a>

        <a href="#">📄 Reportes</a>

        <a href="#">📥 Exportar</a>

        <a href="#">⚙ Configuración</a>

    </nav>

    <div class="sidebar-footer">

        <div>Gemini 2.5 Flash</div>

        <div class="online">

            🟢 ONLINE

        </div>

    </div>

</aside>
""".strip()