"""
core/knowledge/knowledge_base.py

Enterprise Knowledge Base

Construye una base de conocimiento
del dataset.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from core.business import BusinessRules
from core.knowledge.knowledge_insights import (
    KnowledgeInsights,
)


class KnowledgeBase:
    """
    Base de conocimiento empresarial.

    Contiene:

    - Estadísticas
    - Variables
    - Valores nulos
    - Insights
    - Reglas de negocio
    """

    def __init__(self):

        self._knowledge: dict[str, Any] = {}

        self._insights = KnowledgeInsights()

        self._business = BusinessRules()

        self._summary = ""

        self._business_text = ""

    # =====================================================
    # BUILD
    # =====================================================

    def build(
        self,
        dataframe: pd.DataFrame,
    ) -> None:

        numeric = dataframe.select_dtypes(
            include="number"
        ).columns.tolist()

        categorical = dataframe.select_dtypes(
            exclude="number"
        ).columns.tolist()

        self._knowledge = {

            "rows": len(dataframe),

            "columns": len(dataframe.columns),

            "column_names": dataframe.columns.tolist(),

            "numeric_columns": numeric,

            "categorical_columns": categorical,

            "null_values": dataframe.isnull().sum().to_dict(),

            "statistics": dataframe.describe(
                include="all"
            ).to_dict(),

        }

        # ==========================================
        # GENERAR INSIGHTS
        # ==========================================

        self._summary = self._insights.build_text(
            self._knowledge
        )

        # ==========================================
        # BUSINESS RULES
        # ==========================================

        self._business_text = self._business.build_text(
            dataframe.columns.tolist()
        )

    # =====================================================
    # GET
    # =====================================================

    def get(self) -> dict[str, Any]:

        return self._knowledge

    # =====================================================
    # SUMMARY
    # =====================================================

    def summary(self) -> str:

        return f"""
{self._summary}

----------------------------------------

REGLAS EMPRESARIALES

{self._business_text}
""".strip()

    # =====================================================
    # BUSINESS RULES
    # =====================================================

    def business_rules(self) -> str:

        return self._business_text

    # =====================================================
    # INSIGHTS
    # =====================================================

    def insights(self):

        return self._insights.generate(
            self._knowledge
        )