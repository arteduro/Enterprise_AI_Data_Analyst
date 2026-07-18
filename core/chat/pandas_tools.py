"""
core/chat/pandas_tools.py

Herramientas de análisis mediante Pandas.

Todas las consultas rápidas del Chat se
resuelven aquí sin consumir tokens de IA.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.chat.statistics_tools import StatisticsTools


class PandasTools:
    """
    Colección de utilidades para responder
    preguntas rápidas utilizando Pandas.
    """

    @staticmethod
    def answer(
        dataframe: pd.DataFrame,
        question: str,
    ) -> str:

        q = question.lower()

        # =====================================================
        # ESTADÍSTICAS
        # =====================================================

        statistics_keywords = [

            "promedio",
            "media",
            "mediana",

            "máximo",
            "maximo",

            "mínimo",
            "minimo",

            "suma",

            "desviación",
            "desviacion",

            "estadística",
            "estadisticas",
            "estadísticas",

        ]

        if any(
            keyword in q
            for keyword in statistics_keywords
        ):

            return StatisticsTools.answer(
                dataframe,
                question,
            )

        # =====================================================
        # FILAS
        # =====================================================

        if "filas" in q:

            return (
                f"El dataset contiene "
                f"{len(dataframe):,} filas."
            )

        # =====================================================
        # COLUMNAS
        # =====================================================

        if "columnas" in q:

            return (
                f"El dataset contiene "
                f"{len(dataframe.columns)} columnas."
            )

        # =====================================================
        # NULOS
        # =====================================================

        if "nulos" in q:

            total = int(
                dataframe.isna().sum().sum()
            )

            return (
                f"Existen {total} valores nulos."
            )

        # =====================================================
        # DUPLICADOS
        # =====================================================

        if "duplicados" in q:

            total = int(
                dataframe.duplicated().sum()
            )

            return (
                f"Existen {total} registros duplicados."
            )

        # =====================================================
        # VARIABLES NUMÉRICAS
        # =====================================================

        if (
            "variables" in q
            or "numéricas" in q
            or "numericas" in q
        ):

            cols = dataframe.select_dtypes(
                "number"
            ).columns.tolist()

            if not cols:

                return "No existen variables numéricas."

            return (
                "Variables numéricas:\n\n- "
                + "\n- ".join(cols)
            )

        # =====================================================
        # LISTA DE COLUMNAS
        # =====================================================

        if (
            "lista de columnas" in q
            or "columnas disponibles" in q
        ):

            return "\n".join(
                dataframe.columns.tolist()
            )

        # =====================================================
        # OPERACIÓN NO SOPORTADA
        # =====================================================

        return (
            "Todavía no conozco esa operación.\n"
            "Será incorporada en una próxima versión."
        )