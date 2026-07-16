"""
core/ai/dataset_profiler.py

Perfilador inteligente de datasets.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd


class DatasetProfiler:
    """
    Analiza un DataFrame y devuelve información estructurada
    para que posteriormente Gemini genere insights.
    """

    @staticmethod
    def profile(
        df: pd.DataFrame,
    ) -> dict:
        """
        Devuelve un perfil completo del dataset.
        """

        numeric_columns = (
            df.select_dtypes(
                include="number"
            )
            .columns
            .tolist()
        )

        categorical_columns = (
            df.select_dtypes(
                exclude="number"
            )
            .columns
            .tolist()
        )

        profile = {

            "rows": int(
                len(df)
            ),

            "columns": int(
                len(df.columns)
            ),

            "column_names": df.columns.tolist(),

            "numeric_columns": numeric_columns,

            "categorical_columns": categorical_columns,

            "missing_values": {
                column: int(value)
                for column, value in (
                    df.isnull()
                    .sum()
                    .to_dict()
                    .items()
                )
            },

            "duplicates": int(
                df.duplicated().sum()
            ),

            "memory_usage_mb": float(
                round(
                    df.memory_usage(
                        deep=True
                    ).sum()
                    / 1024
                    / 1024,
                    2,
                )
            ),

        }

        return profile