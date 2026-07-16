"""
core/themes/dashboard_theme.py

Carga y unifica todos los estilos CSS del Dashboard.

Autor: Edgar Arteaga
"""

from pathlib import Path


class DashboardTheme:
    """
    Gestor del tema visual.
    """

    STYLE_FILES = [
        "base.css",
        "layout.css",
        "sidebar.css",
        "header.css",
        "kpis.css",
        "cards.css",
        "footer.css",
        "responsive.css",
    ]

    @classmethod
    def css(cls) -> str:
        """
        Devuelve el CSS completo.
        """

        styles_dir = (
            Path(__file__).parent
            / "styles"
        )

        css_parts = []

        for filename in cls.STYLE_FILES:

            css_file = styles_dir / filename

            if css_file.exists():

                css_parts.append(
                    css_file.read_text(
                        encoding="utf-8"
                    )
                )

        return "\n\n".join(css_parts)