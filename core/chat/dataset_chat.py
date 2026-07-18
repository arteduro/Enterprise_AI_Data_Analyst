"""
core/chat/dataset_chat.py

Motor de conversación con el dataset.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from llm.llm_factory import LLMFactory

from core.chat.intent_detector import (
    Intent,
    IntentDetector,
)

from core.chat.pandas_tools import PandasTools


class DatasetChat:
    """
    Chat inteligente sobre un DataFrame.
    """

    def __init__(self):

        self.llm = LLMFactory.create()

    # ======================================================

    def ask(
        self,
        dataframe: pd.DataFrame,
        question: str,
    ) -> str:
        """
        Responde preguntas sobre un dataset.
        """

        intent = IntentDetector.detect(question)

        # --------------------------------------------------

        if intent == Intent.PANDAS:

            return PandasTools.answer(
                dataframe,
                question,
            )

        # --------------------------------------------------

        return self._answer_with_llm(
            dataframe,
            question,
        )

    # ======================================================

    def _answer_with_llm(
        self,
        dataframe: pd.DataFrame,
        question: str,
    ) -> str:
        """
        Envía la consulta a Gemini.
        """

        preview = dataframe.head(10)

        prompt = f"""
Eres un Enterprise AI Data Analyst.

Columnas:

{list(dataframe.columns)}

Primeras filas:

{preview.to_markdown(index=False)}

Pregunta:

{question}

Responde únicamente utilizando la información
disponible en el dataset.

No inventes información.
"""

        return self.llm.generate(prompt)