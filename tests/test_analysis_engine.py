"""
tests/test_analysis_engine.py

Prueba del AnalysisEngine.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.engines.analysis_engine import AnalysisEngine


def main() -> None:
    """
    Ejecuta una prueba del motor de análisis.
    """

    dataframe = pd.DataFrame(
        {
            "edad": [20, 25, 30, 35, 40],
            "salario": [1500, 2000, 2500, 3000, 3500],
            "ciudad": [
                "Cúcuta",
                "Bogotá",
                "Medellín",
                "Cali",
                "Cúcuta",
            ],
            "contratado": [
                "Sí",
                "No",
                "Sí",
                "Sí",
                "No",
            ],
        }
    )

    engine = AnalysisEngine()

    result = engine.analyze_dataframe(
        dataframe
    )

    print()

    print("===== ANALYSIS ENGINE =====")

    print()

    print(f"Filas: {result.basic.rows}")

    print(f"Columnas: {result.basic.columns}")

    print(
        f"Calidad: {result.quality.quality_score}"
    )

    print(
        f"Problema ML: {result.ml.problem_type}"
    )

    print()

    print("Resumen:")

    print(result.summary)


if __name__ == "__main__":
    main()