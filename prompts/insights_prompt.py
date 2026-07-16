"""
prompts/insights_prompt.py

Construcción del prompt que será enviado a Gemini.

Autor: Edgar Arteaga
"""


class InsightsPrompt:
    """
    Construye el prompt para Gemini utilizando
    el contexto generado por DataProcessor.
    """

    @staticmethod
    def build(context: str) -> str:
        """
        Construye el prompt completo.
        """

        prompt = f"""
# Enterprise AI Data Analyst

Actúa como el motor de inteligencia artificial de Enterprise AI Data Analyst.

Tu única tarea consiste en analizar el contexto proporcionado y generar un informe ejecutivo profesional.

IMPORTANTE

- No expliques quién eres.
- No saludes.
- No uses frases como:
    - "Como Científico de Datos..."
    - "Como Analista..."
    - "Con gusto..."
    - "Voy a analizar..."
    - "A continuación..."

Comienza directamente con el informe.

============================================================
CONTEXTO
============================================================

{context}

============================================================

Genera un informe profesional utilizando exactamente esta estructura:

# Resumen Ejecutivo

Describe brevemente el estado general del dataset.

# Hallazgos Importantes

Presenta los principales descubrimientos encontrados.

# Riesgos Detectados

Describe posibles riesgos, inconsistencias o limitaciones.

# Recomendaciones

Propón acciones concretas basadas únicamente en los datos.

# Próximos Pasos

Indica cuáles deberían ser las siguientes acciones del analista.

Reglas:

- Responde únicamente en español.
- Utiliza Markdown.
- Sé claro, técnico y profesional.
- No inventes información.
- Basa todas las conclusiones únicamente en el contexto recibido.
- No agregues explicaciones fuera del informe.
- No repitas el contexto recibido.
"""

        return prompt