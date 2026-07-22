"""
core/reasoning/reasoning_templates.py

Enterprise Reasoning Templates

Convierte un pipeline de razonamiento
en instrucciones cognitivas para el LLM.

Autor: Edgar Arteaga
"""

from core.reasoning.reasoning_stage import ReasoningStage


_STAGE_TEXT = {

    ReasoningStage.OBSERVE:
        "1. Observa cuidadosamente toda la información disponible antes de emitir cualquier conclusión.",

    ReasoningStage.PATTERN:
        "2. Identifica patrones, relaciones, anomalías y comportamientos relevantes dentro de los datos.",

    ReasoningStage.HYPOTHESIS:
        "3. Formula hipótesis que expliquen los patrones encontrados. No asumas que son verdaderas todavía.",

    ReasoningStage.VALIDATE:
        "4. Valida cada hipótesis utilizando únicamente la evidencia disponible en el contexto. No inventes información.",

    ReasoningStage.IMPACT:
        "5. Evalúa el impacto empresarial, operativo, financiero y estratégico de los hallazgos.",

    ReasoningStage.RISK:
        "6. Identifica riesgos potenciales, incertidumbres y limitaciones del análisis.",

    ReasoningStage.ACTION:
        "7. Propón acciones concretas, priorizadas y justificadas con base en la evidencia.",

    ReasoningStage.KPI:
        "8. Define indicadores (KPIs) que permitan medir el éxito de las recomendaciones."
}


def build_reasoning_prompt(stages: list[ReasoningStage]) -> str:
    """
    Convierte el pipeline en instrucciones
    para el modelo.
    """

    lines = [
        "RAZONA SIGUIENDO ESTE PROCESO:"
    ]

    for stage in stages:
        lines.append(_STAGE_TEXT[stage])

    lines.append(
        "No omitas etapas y no inventes información que no exista en el contexto."
    )

    return "\n".join(lines)
