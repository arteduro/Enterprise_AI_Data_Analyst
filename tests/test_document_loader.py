"""
tests/test_document_loader.py

Pruebas del DocumentLoader.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path
import tempfile

import pandas as pd

from core.document_loader import DocumentLoader
from core.exceptions import (
    DatasetNotFoundError,
    InvalidDatasetFormatError,
)


def main() -> None:
    """
    Ejecuta las pruebas del DocumentLoader.
    """

    loader = DocumentLoader()

    dataframe = pd.DataFrame(
        {
            "edad": [20, 25, 30],
            "salario": [1500, 2000, 2500],
            "ciudad": [
                "Cúcuta",
                "Bogotá",
                "Medellín",
            ],
        }
    )

    with tempfile.TemporaryDirectory() as temp_dir:

        temp_path = Path(temp_dir)

        # ==================================================
        # CSV
        # ==================================================

        csv_file = temp_path / "dataset.csv"

        dataframe.to_csv(
            csv_file,
            index=False,
        )

        csv_df = loader.load(csv_file)

        print()

        print("===== CSV =====")

        print(csv_df)

        # ==================================================
        # JSON
        # ==================================================

        json_file = temp_path / "dataset.json"

        dataframe.to_json(
            json_file,
            orient="records",
        )

        json_df = loader.load(json_file)

        print()

        print("===== JSON =====")

        print(json_df)

        # ==================================================
        # Archivo inexistente
        # ==================================================

        print()

        print("===== ARCHIVO INEXISTENTE =====")

        try:

            loader.load(
                temp_path / "no_existe.csv"
            )

        except DatasetNotFoundError:

            print("[OK] DatasetNotFoundError")

        # ==================================================
        # Formato no soportado
        # ==================================================

        unsupported = temp_path / "archivo.xyz"

        unsupported.write_text(
            "Enterprise AI",
            encoding="utf-8",
        )

        print()

        print("===== FORMATO NO SOPORTADO =====")

        try:

            loader.load(
                unsupported
            )

        except InvalidDatasetFormatError:

            print(
                "[OK] InvalidDatasetFormatError"
            )


if __name__ == "__main__":
    main()