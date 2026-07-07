"""
llm/mock_llm.py

Proveedor simulado para desarrollo.

No consume llamadas a Gemini.

Autor: Edgar Arteaga
"""

from typing import Optional

from llm.base_llm import BaseLLM


class MockLLM(BaseLLM):
    """
    Simula un proveedor LLM.

    Ideal para desarrollo y pruebas.
    """

    def generate(
        self,
        prompt: str,
        context: Optional[str] = None
    ) -> str:

        respuesta = [
            "===== MOCK LLM =====",
            "",
            "Esta respuesta fue generada localmente.",
            "",
            f"Pregunta:",
            prompt,
        ]

        if context:

            respuesta.extend([
                "",
                "Contexto recibido:",
                context
            ])

        respuesta.extend([
            "",
            "Estado:",
            "MockLLM funcionando correctamente."
        ])

        return "\n".join(respuesta)

    def health_check(self) -> bool:
        return True