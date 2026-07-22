"""
core/context/context_compressor.py

Enterprise Context Compressor

Reduce el contexto enviado al LLM
manteniendo únicamente la información
relevante para la consulta.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from core.routing.prompt_router import PromptType
from core.context.semantic_context_selector import SemanticContextSelector


class ContextCompressor:

    def __init__(self):

        self.selector = SemanticContextSelector()

    def compress(
        self,
        dataframe: pd.DataFrame,
        memory: str,
        knowledge: str,
        prompt_type: PromptType,
        question: str,
    ) -> dict:

        rows, cols = dataframe.shape

        result = {
            "rows": rows,
            "cols": cols,
            "memory": memory,
            "knowledge": knowledge,
        }

        # ===========================
        # SHORT
        # ===========================

        if prompt_type == PromptType.SHORT:

            result["columns"] = self.selector.select_columns(
                question,
                dataframe,
            )

            return result

        # ===========================
        # SUMMARY
        # ===========================

        if prompt_type == PromptType.SUMMARY:

            result["columns"] = self.selector.select_columns(
                question,
                dataframe,
            )

            return result

        # ===========================
        # ANALYSIS
        # ===========================

        numeric = dataframe.select_dtypes(
            include="number"
        )

        stats = {}

        for column in numeric.columns:

            stats[column] = {
                "mean": float(
                    numeric[column].mean()
                ),
                "min": float(
                    numeric[column].min()
                ),
                "max": float(
                    numeric[column].max()
                ),
            }

        result["columns"] = self.selector.select_columns(
            question,
            dataframe,
        )

        result["stats"] = stats

        return result