"""
core/routing/route_types.py

Tipos de rutas utilizados por el Enterprise Router.

Autor: Edgar Arteaga
"""

from __future__ import annotations

from enum import Enum


class RouteType(str, Enum):

    UNKNOWN = "unknown"

    LOCAL = "local"

    INTERNAL = "internal"

    SUMMARY = "summary"

    ANALYSIS = "analysis"

    RAG = "rag"

    HYBRID = "hybrid"
