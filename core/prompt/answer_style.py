"""
core/prompt/answer_style.py

Enterprise Answer Style Controller

Controla el estilo de respuesta que debe utilizar
el LLM dependiendo del tipo de prompt.

Autor: Edgar Arteaga
"""

from core.routing.prompt_router import PromptType


class AnswerStyle:

    @staticmethod
    def instructions(prompt_type: PromptType) -> str:

        if prompt_type == PromptType.SHORT:
            return """
INSTRUCCIONES DE RESPUESTA

- Responde únicamente la respuesta.
- Máximo 2 líneas.
- No expliques.
- No hagas introducciones.
- No uses listas.
""".strip()

        if prompt_type == PromptType.SUMMARY:
            return """
INSTRUCCIONES DE RESPUESTA

- Máximo 180 palabras.
- Resume únicamente lo importante.
- No escribas introducción.
- No escribas conclusión.
- Evita repetir información.
""".strip()

        if prompt_type == PromptType.ANALYSIS:
            return """
INSTRUCCIONES DE RESPUESTA

Actúa como un Senior Enterprise Data Analyst.

Genera un análisis profesional y profundo.

Estructura obligatoria:

# Resumen ejecutivo

Explica brevemente el estado general del dataset.

# Hallazgos principales

Describe los hallazgos relevantes apoyándote en los datos.

# Patrones detectados

Explica relaciones, tendencias y comportamientos importantes.

# Riesgos

Identifica problemas potenciales para el negocio.

# Oportunidades

Indica oportunidades de mejora basadas en los datos.

# Recomendaciones priorizadas

Presenta recomendaciones accionables indicando su impacto esperado.

# Próximos análisis sugeridos

Sugiere análisis adicionales que aporten valor.

Puedes utilizar tablas y listas cuando sea útil.

No limites la longitud de la respuesta.
""".strip()

        if prompt_type == PromptType.REPORT:
            return """
INSTRUCCIONES DE RESPUESTA

Genera un informe profesional estructurado.
""".strip()

        return ""
