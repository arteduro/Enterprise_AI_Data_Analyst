"""
core/knowledge/knowledge_insights.py

Enterprise Knowledge Insights Engine

Genera insights automáticos del dataset.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Any


class KnowledgeInsights:
    """
    Generador de conocimiento empresarial.

    A partir de la Knowledge Base produce
    observaciones listas para consumir por Gemini.
    """

    def generate(
        self,
        knowledge: dict[str, Any],
    ) -> list[str]:

        insights: list[str] = []

        # ==========================================
        # TAMAÑO DEL DATASET
        # ==========================================

        rows = knowledge.get("rows", 0)

        cols = knowledge.get("columns", 0)

        insights.append(
            f"El dataset contiene {rows:,} registros y {cols} columnas."
        )

        # ==========================================
        # VARIABLES
        # ==========================================

        numeric = knowledge.get(
            "numeric_columns",
            [],
        )

        categorical = knowledge.get(
            "categorical_columns",
            [],
        )

        insights.append(
            f"Se identificaron {len(numeric)} variables numéricas."
        )

        insights.append(
            f"Se identificaron {len(categorical)} variables categóricas."
        )

        # ==========================================
        # VALORES NULOS
        # ==========================================

        nulls = knowledge.get(
            "null_values",
            {},
        )

        total_nulls = sum(
            nulls.values()
        )

        if total_nulls == 0:

            insights.append(
                "El dataset no contiene valores nulos."
            )

        else:

            insights.append(
                f"Se detectaron {total_nulls} valores nulos."
            )

        # ==========================================
        # COLUMNAS NUMÉRICAS
        # ==========================================

        stats = knowledge.get(
            "statistics",
            {},
        )

        for column in numeric:

            try:

                column_stats = stats[column]

                mean = column_stats.get("mean")

                std = column_stats.get("std")

                minimum = column_stats.get("min")

                maximum = column_stats.get("max")

                if mean is None:
                    continue

                insights.append(

                    (
                        f"{column}: "
                        f"promedio={mean:.2f}, "
                        f"desviación={std:.2f}, "
                        f"mínimo={minimum:.2f}, "
                        f"máximo={maximum:.2f}"
                    )

                )

            except Exception:

                continue

        # ==========================================
        # RESUMEN
        # ==========================================

        insights.append(
            "Knowledge Base generada correctamente."
        )

        return insights

    # ==========================================
    # TEXTO
    # ==========================================

    def build_text(
        self,
        knowledge: dict[str, Any],
    ) -> str:
        """
        Convierte los insights en texto.
        """

        insights = self.generate(
            knowledge
        )

        return "\n".join(
            f"• {item}"
            for item in insights
        )