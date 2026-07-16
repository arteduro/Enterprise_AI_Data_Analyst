"""
core/ai/statistics_engine.py

Motor de estadísticas descriptivas.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd


class StatisticsEngine:
    """
    Calcula estadísticas descriptivas del DataFrame.
    """

    @staticmethod
    def describe(
        df: pd.DataFrame,
    ) -> dict:

        numeric = df.select_dtypes(
            include="number"
        )

        statistics = {}

        for column in numeric.columns:

            statistics[column] = {

                "mean": float(
                    round(
                        numeric[column].mean(),
                        2,
                    )
                ),

                "median": float(
                    round(
                        numeric[column].median(),
                        2,
                    )
                ),

                "std": float(
                    round(
                        numeric[column].std(),
                        2,
                    )
                ),

                "min": float(
                    numeric[column].min()
                ),

                "max": float(
                    numeric[column].max()
                ),

            }

        return statistics

    @staticmethod
    def correlation(
        df: pd.DataFrame,
    ) -> dict:

        numeric = df.select_dtypes(
            include="number"
        )

        if numeric.shape[1] < 2:

            return {}

        correlation = {}

        corr = numeric.corr()

        for column in corr.columns:

            correlation[column] = {}

            for row in corr.index:

                correlation[column][row] = float(
                    round(
                        corr.loc[row, column],
                        3,
                    )
                )

        return correlation