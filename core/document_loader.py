"""
core/document_loader.py

Módulo encargado de cargar documentos y datasets
para Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from pathlib import Path
from typing import Union

import pandas as pd

from config.logging_config import get_logger
from core.exceptions import (
    DatasetNotFoundError,
    InvalidDatasetFormatError
)

logger = get_logger(__name__)


class DocumentLoader:
    """
    Cargador universal de documentos.

    Soporta:

    - CSV
    - Excel (.xlsx, .xls)
    - JSON
    - TXT
    - Parquet

    En futuras versiones:

    - PDF
    - DOCX
    - HTML
    """

    SUPPORTED_FORMATS = {
        ".csv",
        ".xlsx",
        ".xls",
        ".json",
        ".txt",
        ".parquet",
    }

    def load(self, file_path: Union[str, Path]):
        """
        Carga un archivo y devuelve su contenido.
        """

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

        if suffix == ".txt":
            return path.read_text(
                encoding="utf-8"
            )

        if suffix == ".parquet":
            return pd.read_parquet(path)

        raise InvalidDatasetFormatError(
            f"No fue posible cargar {path}"
        )