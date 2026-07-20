"""
core/services/llm_service.py

Servicio de acceso a modelos LLM.

Centraliza toda la comunicación con Gemini.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from typing import Optional

from google.genai.errors import ClientError

from llm.gemini_client import GeminiClient


class LLMService:
    """
    Servicio de acceso a modelos LLM.
    """

    def __init__(self):

        self.client = GeminiClient()

    # =====================================================
    # CONSULTA
    # =====================================================

    def ask(
        self,
        question: str,
        context: Optional[str] = None,
    ) -> str:
        """
        Envía una consulta a Gemini.
        """

        try:

            return self.client.generate(
                prompt=question,
                context=context,
            )

        except ClientError as e:

            error = str(e)

            # ==========================================
            # CUOTA AGOTADA
            # ==========================================

            if (
                "RESOURCE_EXHAUSTED" in error
                or "429" in error
                or "quota" in error.lower()
            ):

                return """
🧠 **IA Empresarial**

La capacidad de **Gemini** se encuentra temporalmente ocupada.

### Estado

🟡 Servicio disponible parcialmente

Puedes continuar utilizando:

✅ Estadísticas automáticas

✅ Dashboards

✅ Reportes IA

✅ Perfilado del dataset

✅ Chat con herramientas internas

---

La conversación con IA se reanudará automáticamente cuando Google restablezca la cuota disponible.

No es necesario realizar ninguna acción.
"""

            # Otro error del API
            return (
                "⚠️ Gemini respondió con un error temporal.\n\n"
                "Intenta nuevamente en unos minutos."
            )

        except Exception:

            return (
                "⚠️ No fue posible establecer comunicación "
                "con el servicio de IA."
            )