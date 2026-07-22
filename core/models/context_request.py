"""
core/models/context_request.py

Context Request

Objeto que encapsula todo el contexto
necesario para construir prompts.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from core.routing.prompt_router import PromptType


@dataclass(slots=True)
class ContextRequest:

    prompt_type: PromptType

    dataframe: pd.DataFrame

    memory: str

    knowledge: str

    question: str
