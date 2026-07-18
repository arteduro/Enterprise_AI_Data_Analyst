"""
core/chat/statistics_tools.py

Herramientas estadísticas para Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import re

import pandas as pd


class StatisticsTools:
    """
    Operaciones estadísticas utilizando Pandas.

    Todas las respuestas se generan
    localmente sin utilizar un LLM.
    """

    # ======================================================

    @staticmethod
    def answer(
        dataframe: pd.DataFrame,
        question: str,
    ) -> str:

        q = question.lower()

        column = StatisticsTools._find_column(
            dataframe,
            q,
        )

        if column is None:

            return (
                "No pude identificar la columna "
                "sobre la que deseas realizar el cálculo."
            )

        # --------------------------------------------------

        if (
            "promedio" in q
            or "media" in q
        ):

            value = dataframe[column].mean()

            return (
                f"El promedio de '{column}' es "
                f"{value:,.2f}"
            )

        # --------------------------------------------------

        if "mediana" in q:

            value = dataframe[column].median()

            return (
                f"La mediana de '{column}' es "
                f"{value:,.2f}"
            )

        # --------------------------------------------------

        if (
            "máximo" in q
            or "maximo" in q
        ):

            value = dataframe[column].max()

            return (
                f"El valor máximo de '{column}' es "
                f"{value:,.2f}"
            )

        # --------------------------------------------------

        if (
            "mínimo" in q
            or "minimo" in q
        ):

            value = dataframe[column].min()

            return (
                f"El valor mínimo de '{column}' es "
                f"{value:,.2f}"
            )

        # --------------------------------------------------

        if "suma" in q:

            value = dataframe[column].sum()

            return (
                f"La suma de '{column}' es "
                f"{value:,.2f}"
            )

        # --------------------------------------------------

        if (
            "desviación" in q
            or "desviacion" in q
        ):

            value = dataframe[column].std()

            return (
                f"La desviación estándar de '{column}' es "
                f"{value:,.2f}"
            )

        return (
            "No pude identificar la operación estadística."
        )

    # ======================================================

    @staticmethod
    def _find_column(
        dataframe: pd.DataFrame,
        question: str,
    ) -> str | None:
        """
        Busca una columna mencionada
        dentro de la pregunta.
        """

        normalized = re.sub(
            r"[¿?.,;:]",
            "",
            question.lower(),
        )

        for column in dataframe.columns:

            if column.lower() in normalized:

                if pd.api.types.is_numeric_dtype(
                    dataframe[column]
                ):

                    return column

        return None