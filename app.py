"""
app.py

Punto de entrada de Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from core.application.application_service import ApplicationService
from core.dataset_selector import DatasetSelector


def main():

    print("=" * 80)
    print("ENTERPRISE AI DATA ANALYST")
    print("=" * 80)

    selector = DatasetSelector()

    dataset = selector.choose()

    print()
    print(f"Dataset seleccionado : {dataset.name}")
    print()

    app = ApplicationService()

    dashboard = app.analyze(dataset)

    print()
    print("=" * 80)
    print("ANÁLISIS COMPLETADO")
    print("=" * 80)
    print()

    print(f"Dashboard generado : {dashboard}")
    print()


if __name__ == "__main__":
    main()