"""
tests/test_insights_prompt.py

Prueba del Prompt Builder.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.ai.ai_insights_engine import AIInsightsEngine
from prompts.insights_prompt import InsightsPrompt


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

    prompt = InsightsPrompt.build(
        context
    )

    print("\n")
    print("=" * 80)
    print("PROMPT GENERADO")
    print("=" * 80)
    print()
    print(prompt)
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()