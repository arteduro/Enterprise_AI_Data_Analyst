"""
tests/test_data_processor.py

Prueba del DataProcessor.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.data_processor import DataProcessor


def main():
    """
    Ejecuta una prueba completa del DataProcessor.
    """

    df = pd.DataFrame(
        {
            "edad": [20, 25, 30, 35, 40],
            "salario": [1500, 1800, 2200, 2600, 3000],
            "departamento": [
                "Ventas",
                "TI",
                "TI",
                "RRHH",
                "Ventas",
            ],
            "contratado": [
                "Sí",
                "Sí",
                "No",
                "Sí",
                "No",
            ],
        }
    )

    processor = DataProcessor()

    result = processor.profile(df)

    print()
    print("===== DATA PROCESSOR =====")
    print()

    print("Filas:", result.basic.rows)
    print("Columnas:", result.basic.columns)
    print("Variables numéricas:", result.basic.numeric_columns)
    print("Variables categóricas:", result.basic.categorical_columns)
    print()

    print("Calidad:", result.quality.quality_score)
    print("Valores nulos:", result.quality.missing_values)
    print("Duplicados:", result.quality.duplicated_rows)
    print()

    print("Problema ML:", result.ml.problem_type)
    print("Target:", result.ml.possible_target)
    print()

    print("Resumen:")
    print(result.summary)
    print()

    print("Recomendaciones:")

    for recommendation in result.recommendations:
        print("-", recommendation)

    print()
    print("===== AI CONTEXT =====")
    print()
    print(result.ai_context)


if __name__ == "__main__":
    main()