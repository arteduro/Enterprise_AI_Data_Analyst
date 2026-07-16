"""
core/components/dashboard_footer.py

Footer del Dashboard.

Autor: Edgar Arteaga
"""


class DashboardFooter:
    """
    Componente Footer.
    """

    @staticmethod
    def render() -> str:

        return """
<footer>

    <p>
        Enterprise AI Data Analyst © 2026
    </p>

</footer>
"""