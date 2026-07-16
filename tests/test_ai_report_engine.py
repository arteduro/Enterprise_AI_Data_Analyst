"""
tests/test_ai_report_engine.py

Prueba del AIReportEngine.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.ai.ai_report_engine import AIReportEngine


def main():

    df = pd.DataFrame(
        {
            "edad": [20, 25, 30, 40],
            "salario": [1200, 1800, 2500, 4000],
            "ventas": [10, 15, 20, 28],
            "ciudad": [
                "Cúcuta",
                "Bogotá",
                "Medellín",
                "Cali",
            ],
        }
    )

    engine = AIReportEngine()

    result = engine.generate_report(df)

    print()
    print("=" * 80)
    print("AI REPORT ENGINE")
    print("=" * 80)

    print("\nMODELO")
    print("-" * 80)
    print(result.model)

    print("\nTIEMPO DE EJECUCION")
    print("-" * 80)
    print(f"{result.execution_time:.4f} segundos")

    print("\nPROMPT")
    print("-" * 80)
    print(result.prompt)

    print("\nREPORTE")
    print("-" * 80)
    print(result.report)

    print()
    print("=" * 80)


if __name__ == "__main__":
    main()