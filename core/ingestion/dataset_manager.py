"""
core/ingestion/dataset_manager.py

Administrador central de datasets.

Responsabilidades
-----------------
- Mantener el dataset activo.
- Gestionar el Dataset Demo.
- Gestionar datasets cargados por el usuario.
- Exponer la ruta del dataset activo.
- Listar datasets disponibles.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path


class DatasetManager:
    """
    Administra los datasets disponibles
    dentro de la plataforma.
    """

    # ---------------------------------------------------------
    # Carpetas
    # ---------------------------------------------------------

    DEMO_FOLDER = Path("datasets/demo")

    UPLOADED_FOLDER = Path("datasets/uploaded")

    REGISTRY_FOLDER = Path("datasets/registry")

    # ---------------------------------------------------------
    # Dataset Demo
    # ---------------------------------------------------------

    DEMO_DATASET = DEMO_FOLDER / "ventas.xlsx"

    # ---------------------------------------------------------
    # Formatos soportados
    # ---------------------------------------------------------

    SUPPORTED_FORMATS = {
        ".csv",
        ".xlsx",
        ".xls",
        ".json",
        ".parquet",
    }

    # ---------------------------------------------------------
    # Constructor
    # ---------------------------------------------------------

    def __init__(self) -> None:

        self._active_dataset: Path = self.DEMO_DATASET

    # ---------------------------------------------------------
    # Dataset activo
    # ---------------------------------------------------------

    def get_active_dataset(self) -> Path:
        """
        Devuelve la ruta del dataset activo.
        """

        return self._active_dataset

    def set_active_dataset(
        self,
        dataset_path: str | Path,
    ) -> None:
        """
        Cambia el dataset activo.
        """

        self._active_dataset = Path(dataset_path)

    def activate_dataset(
        self,
        dataset_path: str | Path,
    ) -> None:
        """
        Alias semántico de set_active_dataset().
        """

        self.set_active_dataset(dataset_path)

    # ---------------------------------------------------------
    # Dataset Demo
    # ---------------------------------------------------------

    def use_demo_dataset(self) -> None:
        """
        Activa el dataset demo.
        """

        self._active_dataset = self.DEMO_DATASET

    def get_demo_dataset(self) -> Path:
        """
        Devuelve el dataset demo.
        """

        return self.DEMO_DATASET

    def is_demo_dataset(self) -> bool:
        """
        Indica si el dataset activo
        corresponde al dataset demo.
        """

        return self._active_dataset == self.DEMO_DATASET

    # ---------------------------------------------------------
    # Datasets disponibles
    # ---------------------------------------------------------

    def list_available_datasets(self) -> list[Path]:
        """
        Lista todos los datasets
        disponibles (demo + usuario).
        """

        datasets: list[Path] = []

        for folder in (
            self.DEMO_FOLDER,
            self.UPLOADED_FOLDER,
        ):

            if not folder.exists():
                continue

            for extension in self.SUPPORTED_FORMATS:

                datasets.extend(
                    folder.glob(f"*{extension}")
                )

        return sorted(datasets)

    def get_uploaded_datasets(self) -> list[Path]:
        """
        Devuelve únicamente
        los datasets cargados
        por el usuario.
        """

        datasets: list[Path] = []

        if not self.UPLOADED_FOLDER.exists():
            return datasets

        for extension in self.SUPPORTED_FORMATS:

            datasets.extend(
                self.UPLOADED_FOLDER.glob(f"*{extension}")
            )

        return sorted(datasets)

    # ---------------------------------------------------------
    # Información
    # ---------------------------------------------------------

    def dataset_name(self) -> str:
        """
        Nombre del dataset activo.
        """

        return self._active_dataset.name

    def dataset_location(self) -> Path:
        """
        Carpeta donde se encuentra
        el dataset activo.
        """

        return self._active_dataset.parent

    def dataset_exists(self) -> bool:
        """
        Verifica que exista el dataset activo.
        """

        return self._active_dataset.exists()