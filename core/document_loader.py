"""
core/document_loader.py

Cargador universal de datasets.

Autor: Edgar Arteaga
"""

from pathlib import Path
from typing import Union

import pandas as pd

from config.logging_config import get_logger
from core.exceptions import (
    DatasetNotFoundError,
    InvalidDatasetFormatError,
)

logger = get_logger(__name__)


class DocumentLoader:
    """
    Cargador universal de documentos.
    """

    DATASET_FOLDER = Path("datasets")

    SUPPORTED_FORMATS = {
        ".csv",
        ".xlsx",
        ".xls",
        ".json",
        ".parquet",
    }

    def load(
        self,
        file_path: Union[str, Path],
    ):

        path = Path(file_path)

        logger.info(f"Cargando archivo: {path}")

        if not path.exists():
            raise DatasetNotFoundError(
                f"No existe el archivo: {path}"
            )

        suffix = path.suffix.lower()

        if suffix not in self.SUPPORTED_FORMATS:
            raise InvalidDatasetFormatError(
                f"Formato no soportado: {suffix}"
            )

        if suffix == ".csv":
            return pd.read_csv(path)

        if suffix in [".xlsx", ".xls"]:
            return pd.read_excel(path)

        if suffix == ".json":
            return pd.read_json(path)

        if suffix == ".parquet":
            return pd.read_parquet(path)

        raise InvalidDatasetFormatError(
            f"No fue posible cargar {path}"
        )

    def find_datasets(self) -> list[Path]:
        """
        Devuelve todos los datasets encontrados.
        """

        datasets = []

        if not self.DATASET_FOLDER.exists():
            return datasets

        for extension in self.SUPPORTED_FORMATS:

            datasets.extend(
                self.DATASET_FOLDER.glob(f"*{extension}")
            )

        return sorted(datasets)

    def find_first_dataset(self) -> Path:
        """
        Devuelve el primer dataset disponible.
        """

        datasets = self.find_datasets()

        if not datasets:
            raise DatasetNotFoundError(
                "No se encontró ningún dataset."
            )

        logger.info(
            f"Dataset encontrado: {datasets[0].name}"
        )

        return datasets[0]