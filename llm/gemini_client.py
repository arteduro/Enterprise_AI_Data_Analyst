"""
llm/gemini_client.py

Cliente oficial para Google Gemini utilizando
el SDK moderno google-genai.

Autor: Edgar Arteaga
"""

from typing import Optional

from google import genai
from google.genai import types

from config.settings import settings
from config.logging_config import get_logger
from llm.base_llm import BaseLLM

logger = get_logger(__name__)


class GeminiClient(BaseLLM):
    """
    Cliente para interactuar con Google Gemini.
    """

    def __init__(self):

        if not settings.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY no está configurada."
            )

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        logger.info(
            f"Gemini inicializado ({settings.GEMINI_MODEL})"
        )

    def generate(
        self,
        prompt: str,
        context: Optional[str] = None,
        max_output_tokens: int = 512,
    ) -> str:

        if context:

            prompt = (
                f"Contexto:\n"
                f"{context}\n\n"
                f"Pregunta:\n"
                f"{prompt}"
            )

        logger.info("Consultando Gemini...")
        print(f"[Gemini] max_output_tokens = {max_output_tokens}")

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                top_p=0.9,
                max_output_tokens=max_output_tokens,
            ),
        )

        logger.info("Respuesta recibida.")

        print("\n===== GEMINI DEBUG =====")

        try:
            candidate = response.candidates[0]

            print("Finish reason:", candidate.finish_reason)

            if hasattr(candidate, "token_count"):
                print("Token count:", candidate.token_count)

        except Exception as e:
            print("No fue posible obtener finish_reason:", e)

        print("========================\n")

        return response.text

    def health_check(self) -> bool:
        """
        Comprueba que Gemini responde correctamente.
        """

        try:

            self.generate("Responde únicamente: OK")

            return True

        except Exception as e:

            logger.exception(e)

            return False