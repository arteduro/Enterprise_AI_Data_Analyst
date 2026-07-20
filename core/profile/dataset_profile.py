"""
core/profile/dataset_profile.py

Modelo que almacena el perfil completo
del dataset.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class DatasetProfile:

    rows: int

    columns: int

    numeric_columns: list[str]

    categorical_columns: list[str]

    missing_values: int

    describe: pd.DataFrame

    dataframe: pd.DataFrame