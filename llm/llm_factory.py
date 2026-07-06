"""
llm/llm_factory.py

Factory para obtener el proveedor LLM configurado.

Autor: Edgar Arteaga
"""

from config.settings import settings

from llm.base_llm import BaseLLM
from llm.gemini_client import GeminiClient
from llm.provider import ModelProvider


class LLMFactory:
    """
    Crea la instancia del proveedor LLM configurado.
    """

    @staticmethod
    def create() -> BaseLLM:

        provider = ModelProvider(
            settings.MODEL_PROVIDER.lower()
        )

        match provider:

            case ModelProvider.GOOGLE:
                return GeminiClient()

            case _:
                raise ValueError(
                    f"Proveedor no soportado: {provider.value}"
                )