"""
tests/test_enterprise_ai_dataframe.py

Prueba de EnterpriseAI utilizando
un DataFrame en memoria.

Autor: Edgar Arteaga
"""

import pandas as pd

from core.enterprise_ai import EnterpriseAI


def main() -> None:
    """
    Ejecuta la prueba del flujo completo
    usando un DataFrame.
    """

    dataframe = pd.DataFrame(
        {
            "edad": [20, 25, 30, 40, 35],
            "salario": [1500, 2000, 3000, 5000, 4500],
            "ciudad": [
                "Cúcuta",
                "Bogotá",
                "Medellín",
                "Cali",
                "Cúcuta",
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

    ai = EnterpriseAI()

    response = ai.ask_dataframe(
        dataframe,
        "¿Qué algoritmo de Machine Learning recomiendas para este dataset?",
    )

    print("\n===== ENTERPRISE AI (DATAFRAME) =====\n")

    print("===== RESPUESTA =====\n")

    print(response)


if __name__ == "__main__":
    main()