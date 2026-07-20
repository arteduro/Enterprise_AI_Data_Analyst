"""
core/profile/profiler.py

Construye un DatasetProfile a partir
de un DataFrame.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.profile.dataset_profile import (
    DatasetProfile,
)


class DatasetProfiler:
    """
    Generador del perfil del dataset.
    """

    def build(
        self,
        dataframe: pd.DataFrame,
    ) -> DatasetProfile:
        """
        Analiza el DataFrame una sola vez.
        """

        numeric = dataframe.select_dtypes(
            include="number"
        )

        categorical = dataframe.select_dtypes(
            exclude="number"
        )

        profile = DatasetProfile(

            rows=len(dataframe),

            columns=len(dataframe.columns),

            numeric_columns=list(
                numeric.columns
            ),

            categorical_columns=list(
                categorical.columns
            ),

            missing_values=int(
                dataframe.isna().sum().sum()
            ),

            describe=numeric.describe().round(2),

            dataframe=dataframe,
        )

        return profile