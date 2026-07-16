"""
tests/test_ai_insights_engine.py

Prueba del AIInsightsEngine.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pprint

import pandas as pd

from core.ai.ai_insights_engine import AIInsightsEngine


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

    context = AIInsightsEngine.build_context(df)

    print("\n===== AI INSIGHTS ENGINE =====\n")

    pprint.pprint(
        context,
        sort_dicts=False,
        width=120,
    )


if __name__ == "__main__":
    main()