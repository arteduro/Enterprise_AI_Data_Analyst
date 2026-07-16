"""
tests/test_enterprise_engine.py

Prueba completa del EnterpriseEngine.

Autor: Edgar Arteaga
"""

from pathlib import Path

import pandas as pd

from core.engines.enterprise_engine import EnterpriseEngine


def main() -> None:
    """
    Ejecuta el flujo completo.
    """

    dataframe = pd.DataFrame(
        {
            "edad": [20, 25, 30, 40, 35],
            "salario": [1500, 2000, 3000, 5000, 4500],
            "ventas": [10, 15, 20, 30, 28],
            "ciudad": [
                "Cúcuta",
                "Bogotá",
                "Medellín",
                "Cali",
                "Cúcuta",
            ],
        }
    )

    engine = EnterpriseEngine()

    output = engine.analyze_dataframe(dataframe)

    print("\n===== ENTERPRISE ENGINE =====\n")

    print(f"Dashboard generado: {output}")

    print(f"Existe: {Path(output).exists()}")

    print("\nEnterprise Engine ejecutado correctamente.")


if __name__ == "__main__":
    main()