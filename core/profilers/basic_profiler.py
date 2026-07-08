"""
core/profilers/basic_profiler.py

Perfilador básico de datasets.

Obtiene información general del DataFrame.

Autor: Edgar Arteaga
"""

from dataclasses import dataclass

import pandas as pd


# ==========================================================
# Perfil básico del dataset
# ==========================================================

@dataclass
class BasicProfile:
    """
    Contiene la información básica de un dataset.
    """

    rows: int

    columns: int

    numeric_columns: int

    categorical_columns: int

    datetime_columns: int

    boolean_columns: int

    memory_usage_mb: float

    dtypes: dict[str, str]


# ==========================================================
# Perfilador básico
# ==========================================================

class BasicProfiler:
    """
    Genera un perfil básico del DataFrame.
    """

    def analyze(
        self,
        df: pd.DataFrame
    ) -> BasicProfile:
        """
        Analiza un DataFrame y devuelve un perfil básico.
        """

        return BasicProfile(

            rows=len(df),

            columns=len(df.columns),

            numeric_columns=len(
                df.select_dtypes(
                    include="number"
                ).columns
            ),

            categorical_columns=len(
                df.select_dtypes(
                    include="object"
                ).columns
            ),

            datetime_columns=len(
                df.select_dtypes(
                    include="datetime"
                ).columns
            ),

            boolean_columns=len(
                df.select_dtypes(
                    include="bool"
                ).columns
            ),

            memory_usage_mb=round(
                df.memory_usage(
                    deep=True
                ).sum() / 1024 / 1024,
                2
            ),

            dtypes={
                column: str(dtype)
                for column, dtype in df.dtypes.items()
            }

        )