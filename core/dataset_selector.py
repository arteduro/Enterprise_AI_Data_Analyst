"""
core/dataset_selector.py

Selector de datasets disponibles.

Autor: Edgar Arteaga
"""

from pathlib import Path

from core.document_loader import DocumentLoader


class DatasetSelector:
    """
    Permite listar y seleccionar datasets disponibles.
    """

    def __init__(self):

        self.loader = DocumentLoader()

    def list_datasets(self):

        datasets = sorted(self.loader.find_datasets())

        return datasets

    def choose(self) -> Path:

        datasets = self.list_datasets()

        if not datasets:
            raise FileNotFoundError(
                "No existen datasets disponibles."
            )

        print("\n")
        print("=" * 70)
        print("DATASETS DISPONIBLES")
        print("=" * 70)
        print()

        for i, dataset in enumerate(datasets, start=1):
            print(f"[{i}] {dataset.name}")

        print()

        while True:

            try:

                option = int(
                    input("Seleccione un dataset: ")
                )

                if 1 <= option <= len(datasets):

                    return datasets[option - 1]

            except ValueError:
                pass

            print("Opción inválida.\n")