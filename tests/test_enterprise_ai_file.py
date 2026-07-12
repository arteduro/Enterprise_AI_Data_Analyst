"""
tests/test_enterprise_ai_file.py

Prueba de integración para EnterpriseAI.

Valida el flujo completo:

CSV
 ↓
DocumentLoader
 ↓
AnalysisEngine
 ↓
DataProcessor
 ↓
AnalysisResult
 ↓
EnterpriseAI
 ↓
LLM

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path
import tempfile

import pandas as pd

from core.enterprise_ai import EnterpriseAI


def main() -> None:
    """
    Ejecuta una prueba completa de EnterpriseAI
    utilizando un dataset temporal.
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
                "Barranquilla",
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

    with tempfile.TemporaryDirectory() as temp_dir:

        dataset_path = (
            Path(temp_dir)
            / "empleados.csv"
        )

        dataframe.to_csv(
            dataset_path,
            index=False,
        )

        ai = EnterpriseAI()

        print()

        print("===== ENTERPRISE AI =====")

        response = ai.ask_file(
            file_path=str(dataset_path),
            question=(
                "¿Qué algoritmo de Machine Learning "
                "recomiendas para este dataset?"
            ),
        )

        print()

        print("===== RESPUESTA =====")

        print()

        print(response)


if __name__ == "__main__":
    main()