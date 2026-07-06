"""
llm/base_llm.py

Clase base para cualquier proveedor de modelos
de lenguaje (LLM).

Todos los proveedores (Gemini, OpenAI,
Anthropic, Ollama...) deberán implementar
esta interfaz.

Autor: Edgar Arteaga
"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseLLM(ABC):
    """
    Interfaz base para todos los modelos LLM.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        context: Optional[str] = None
    ) -> str:
        """
        Genera una respuesta utilizando un modelo.
        """
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """
        Comprueba que el proveedor responde.
        """
        pass