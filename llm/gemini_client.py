"""
llm/gemini_client.py

Cliente oficial para Google Gemini utilizando
el SDK moderno google-genai.

Autor: Edgar Arteaga
"""

from typing import Optional

from google import genai

from config.settings import settings
from config.logging_config import get_logger

logger = get_logger(__name__)


class GeminiClient:
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
        context: Optional[str] = None
    ) -> str:

        if context:

            prompt = (
                f"Contexto:\n"
                f"{context}\n\n"
                f"Pregunta:\n"
                f"{prompt}"
            )

        logger.info("Consultando Gemini...")

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
        )

        logger.info("Respuesta recibida.")

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