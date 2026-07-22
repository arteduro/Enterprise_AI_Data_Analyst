"""
core/monitoring/token_optimizer.py

Enterprise Token Optimizer

Monitorea el uso del Router y estima
el ahorro de tokens.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import time

from core.routing.route_types import RouteType


class TokenOptimizer:
    """
    Monitorea el uso de Gemini
    y estima ahorro de tokens.
    """

    def __init__(self):

        self.reset()

    # =====================================================
    # CONTROL
    # =====================================================

    def start(self):

        self._start = time.perf_counter()

    def finish(self):

        self.elapsed_ms = (
            time.perf_counter() - self._start
        ) * 1000

    def reset(self):

        self.route = RouteType.UNKNOWN

        self.elapsed_ms = 0.0

        self.used_gemini = False

        self.estimated_tokens = 0

        self.saved_tokens = 0

    # =====================================================
    # CONFIGURACIÓN
    # =====================================================

    def configure(
        self,
        route: RouteType,
    ):

        self.route = route

        # -----------------------------------------
        # LOCAL
        # -----------------------------------------

        if route == RouteType.LOCAL:

            self.used_gemini = False

            self.estimated_tokens = 0

            self.saved_tokens = 1200

        # -----------------------------------------
        # INTERNAL
        # -----------------------------------------

        elif route == RouteType.INTERNAL:

            self.used_gemini = False

            self.estimated_tokens = 0

            self.saved_tokens = 900

        # -----------------------------------------
        # SUMMARY
        # -----------------------------------------

        elif route == RouteType.SUMMARY:

            self.used_gemini = True

            self.estimated_tokens = 600

            self.saved_tokens = 600

        # -----------------------------------------
        # ANALYSIS
        # -----------------------------------------

        elif route == RouteType.ANALYSIS:

            self.used_gemini = True

            self.estimated_tokens = 1800

            self.saved_tokens = 0

        # -----------------------------------------
        # RAG
        # -----------------------------------------

        elif route == RouteType.RAG:

            self.used_gemini = True

            self.estimated_tokens = 1400

            self.saved_tokens = 300

        # -----------------------------------------
        # HYBRID
        # -----------------------------------------

        elif route == RouteType.HYBRID:

            self.used_gemini = True

            self.estimated_tokens = 2200

            self.saved_tokens = 400

    # =====================================================
    # MÉTRICAS
    # =====================================================

    def metrics(self):

        return {

            "route": self.route.value,

            "elapsed_ms": round(
                self.elapsed_ms,
                2,
            ),

            "used_gemini": self.used_gemini,

            "estimated_tokens": self.estimated_tokens,

            "saved_tokens": self.saved_tokens,

        }

    # =====================================================
    # RESUMEN
    # =====================================================

    def summary(self) -> str:

        gemini = (
            "Sí"
            if self.used_gemini
            else "No"
        )

        return f"""
⚡ Enterprise AI Router

Ruta:
{self.route.value.upper()}

Tiempo:
{self.elapsed_ms:.1f} ms

Gemini:
{gemini}

Tokens estimados:
{self.estimated_tokens:,}

Ahorro estimado:
{self.saved_tokens:,}
""".strip()