"""
core/formatters/context_formatter.py

Formateador de contexto para modelos LLM.

Autor: Edgar Arteaga
"""

from __future__ import annotations


class ContextFormatter:
    """
    Convierte el contexto generado por AIInsightsEngine
    en un texto limpio y legible para los modelos LLM.
    """

    @staticmethod
    def format(context: dict) -> str:

        profile = context["profile"]
        statistics = context["statistics"]
        correlations = context["correlations"]

        lines = []

        # =====================================================
        # INFORMACIÓN GENERAL
        # =====================================================

        lines.append("INFORMACION GENERAL")
        lines.append("=" * 60)

        lines.append(f"Filas: {profile['rows']}")
        lines.append(f"Columnas: {profile['columns']}")

        lines.append(
            "Variables numericas: "
            + ", ".join(profile["numeric_columns"])
        )

        lines.append(
            "Variables categoricas: "
            + ", ".join(profile["categorical_columns"])
        )

        lines.append(f"Duplicados: {profile['duplicates']}")
        lines.append(f"Uso de memoria (MB): {profile['memory_usage_mb']}")

        # =====================================================
        # NULOS
        # =====================================================

        lines.append("")
        lines.append("VALORES NULOS")
        lines.append("-" * 60)

        for column, value in profile["missing_values"].items():
            lines.append(f"- {column}: {value}")

        # =====================================================
        # ESTADÍSTICAS
        # =====================================================

        lines.append("")
        lines.append("ESTADISTICAS DESCRIPTIVAS")
        lines.append("=" * 60)

        for column, values in statistics.items():

            lines.append("")
            lines.append(f"Variable: {column}")

            lines.append(f"   - Media: {values['mean']}")
            lines.append(f"   - Mediana: {values['median']}")
            lines.append(f"   - Desviacion estandar: {values['std']}")
            lines.append(f"   - Minimo: {values['min']}")
            lines.append(f"   - Maximo: {values['max']}")

        # =====================================================
        # CORRELACIONES
        # =====================================================

        lines.append("")
        lines.append("CORRELACIONES")
        lines.append("=" * 60)

        shown = set()

        for col1, values in correlations.items():

            for col2, corr in values.items():

                if col1 == col2:
                    continue

                pair = tuple(sorted((col1, col2)))

                if pair in shown:
                    continue

                shown.add(pair)

                lines.append(
                    f"- {col1} <-> {col2}: {corr}"
                )

        return "\n".join(lines)