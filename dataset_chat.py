"""
core/chat/dataset_chat.py

Motor de conversación con el dataset.

Permite responder preguntas utilizando
Pandas o IA dependiendo de la intención.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Any

import pandas as pd


class DatasetChat:
    """
    Chat inteligente sobre un DataFrame.
    """

    def __init__(self, dataframe: pd.DataFrame, llm=None):

        self.dataframe = dataframe

        self.llm = llm

    # ======================================================
    # API PRINCIPAL
    # ======================================================

    def ask(self, question: str) -> str:
        """
        Responde una pregunta del usuario.
        """

        question = question.strip()

        if not question:

            return "Escribe una pregunta."

        lower = question.lower()

        # -------------------------------
        # FILAS
        # -------------------------------

        if "filas" in lower:

            return (
                f"El dataset contiene "
                f"{len(self.dataframe):,} filas."
            )

        # -------------------------------
        # COLUMNAS
        # -------------------------------

        if "columnas" in lower:

            return (
                f"El dataset contiene "
                f"{len(self.dataframe.columns)} columnas."
            )

        # -------------------------------
        # VARIABLES NUMERICAS
        # -------------------------------

        if (
            "variables numéricas" in lower
            or "variables numericas" in lower
            or "numéricas" in lower
            or "numericas" in lower
        ):

            cols = self.dataframe.select_dtypes(
                "number"
            ).columns.tolist()

            return (
                "Variables numéricas:\n\n- "
                + "\n- ".join(cols)
            )

        # -------------------------------
        # NULOS
        # -------------------------------

        if "nulos" in lower:

            total = int(
                self.dataframe.isna().sum().sum()
            )

            return (
                f"El dataset contiene "
                f"{total} valores nulos."
            )

        # -------------------------------
        # COLUMNAS
        # -------------------------------

        if "lista de columnas" in lower:

            return (
                "\n".join(self.dataframe.columns)
            )

        # -------------------------------
        # IA
        # -------------------------------

        if self.llm is not None:

            prompt = self._build_prompt(question)

            return self.llm.generate(prompt)

        return (
            "Todavía no puedo responder esa pregunta.\n\n"
            "En la siguiente versión utilizaré IA "
            "para responder preguntas complejas."
        )

    # ======================================================
    # PROMPT
    # ======================================================

    def _build_prompt(
        self,
        question: str,
    ) -> str:
        """
        Construye el contexto enviado al LLM.
        """

        preview = self.dataframe.head(10)

        return f"""
Eres un Analista de Datos Empresarial.

Columnas:

{list(self.dataframe.columns)}

Primeras filas:

{preview.to_markdown(index=False)}

Pregunta:

{question}

Responde de forma profesional.
"""