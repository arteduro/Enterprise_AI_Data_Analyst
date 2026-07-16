"""
core/components/ai_report_card.py

Componente que renderiza el informe generado por IA.

Autor: Edgar Arteaga
"""


class AIReportCard:
    """
    Renderiza el reporte generado por Gemini.
    """

    @staticmethod
    def render(report: str) -> str:

        if not report:

            report = (
                "Aún no se ha generado ningún informe."
            )

        return f"""
<div class="card ai-report-card">

    <h2>🤖 Análisis Inteligente</h2>

    <div class="ai-report">

        {report}

    </div>

</div>
"""