"""
core/context/context_builder.py

Construye el contexto enviado al LLM.

Versión 2 basada en DatasetProfile.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from core.profile import DatasetProfile


class ContextBuilder:
    """
    Construye el contexto para Gemini utilizando
    el DatasetProfile previamente calculado.
    """

    def build(
        self,
        profile: DatasetProfile,
        memory: str,
        question: str,
    ) -> str:

        context = f"""
==============================
DATASET
==============================

Filas:
{profile.rows}

Columnas:
{profile.columns}

Variables numéricas:
{", ".join(profile.numeric_columns)}

Variables categóricas:
{", ".join(profile.categorical_columns)}

Valores nulos:
{profile.missing_values}

==============================
ESTADÍSTICAS
==============================

{profile.describe.to_string()}

==============================
HISTORIAL
==============================

{memory}

==============================
PREGUNTA
==============================

{question}
"""

        return context.strip()