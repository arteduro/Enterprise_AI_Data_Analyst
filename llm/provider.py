"""
llm/provider.py

Enumeración de proveedores LLM soportados.

Autor: Edgar Arteaga
"""

from enum import Enum


class ModelProvider(str, Enum):
    """
    Proveedores soportados por Enterprise AI Data Analyst.
    """

    GOOGLE = "google"

    OPENAI = "openai"

    ANTHROPIC = "anthropic"

    AZURE = "azure"

    OLLAMA = "ollama"