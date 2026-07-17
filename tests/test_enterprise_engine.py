"""
tests/test_enterprise_engine.py

Prueba completa del EnterpriseEngine.

Carga automáticamente el primer dataset encontrado
en la carpeta datasets.

Autor: Edgar Arteaga
"""

from pathlib import Path

from core.document_loader import DocumentLoader
from core.engines.enterprise_engine import EnterpriseEngine


def main() -> None:
    """
    Ejecuta el flujo completo.
    """

    loader = DocumentLoader()

    dataset = loader.find_first_dataset()

    dataframe = loader.load(dataset)

    engine = EnterpriseEngine()

    output = engine.analyze_dataframe(dataframe)

    print("\n" + "=" * 80)
    print("ENTERPRISE AI DATA ANALYST")
    print("=" * 80)

    print(f"\nDataset utilizado : {dataset.name}")

    print(f"Ruta             : {dataset}")

    print(f"Filas            : {len(dataframe):,}")

    print(f"Columnas         : {len(dataframe.columns)}")

    print()

    print(f"Dashboard        : {output}")

    print(f"Existe           : {Path(output).exists()}")

    print("\nPipeline ejecutado correctamente.")


if __name__ == "__main__":
    main()