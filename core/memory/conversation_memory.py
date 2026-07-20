"""
core/memory/conversation_memory.py

Memoria conversacional.

Guarda el historial de la conversación
entre el usuario y la IA.

Autor: Edgar Arteaga
"""

from __future__ import annotations


class ConversationMemory:
    """
    Memoria simple de conversación.

    Será utilizada posteriormente por:

    - Gemini
    - RAG
    - Agentes
    - MultiLLM
    """

    def __init__(self):

        self.history = []

    # =====================================================
    # USUARIO
    # =====================================================

    def add_user_message(
        self,
        message: str,
    ):

        self.history.append(
            {
                "role": "user",
                "content": message,
            }
        )

    # =====================================================
    # IA
    # =====================================================

    def add_assistant_message(
        self,
        message: str,
    ):

        self.history.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    # =====================================================
    # HISTORIAL
    # =====================================================

    def messages(self):

        return self.history

    # =====================================================
    # CONTEXTO
    # =====================================================

    def build_context(self) -> str:

        if not self.history:

            return ""

        context = ""

        for item in self.history:

            role = item["role"]

            content = item["content"]

            context += f"{role}: {content}\n"

        return context

    # =====================================================
    # LIMPIAR
    # =====================================================

    def clear(self):

        self.history.clear()