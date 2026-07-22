"""
core/services/llm_service.py

Servicio de acceso a modelos LLM.

Centraliza toda la comunicación con Gemini.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import math

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
    # TOKEN ESTIMATION
    # =====================================================

    @staticmethod
    def estimate_tokens(text: str | None) -> int:

        if not text:
            return 0

        # Aproximación: 1 token ≈ 4 caracteres
        return math.ceil(len(text) / 4)


    # =====================================================
    # CONSULTA
    # =====================================================

    def ask(
        self,
        question: str,
        context: Optional[str] = None,
        max_output_tokens: int = 1024,
    ) -> str:
        """
        Envía una consulta a Gemini.
        """

        try:

            # ==========================================
            # TOKEN ESTIMATION
            # ==========================================

            question_tokens = self.estimate_tokens(
                question
            )

            context_tokens = self.estimate_tokens(
                context
            )

            total_tokens = (
                question_tokens
                + context_tokens
            )

            print(
                f"""
==============================
ENTERPRISE TOKEN MONITOR
==============================

Pregunta........ {question_tokens}
Contexto........ {context_tokens}
TOTAL........... {total_tokens}
==============================
""".strip()
            )


            return self.client.generate(
                prompt=question,
                context=context,
                max_output_tokens=max_output_tokens,
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
