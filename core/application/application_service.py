"""
core/application/application_service.py

Capa de aplicación de Enterprise AI Data Analyst.

Expone un punto único de entrada para cualquier
interfaz (CLI, Streamlit, FastAPI, Desktop, etc.).

Autor: Edgar Arteaga
"""

from __future__ import annotations

from pathlib import Path

from core.engines.enterprise_engine import EnterpriseEngine


class ApplicationService:
    """
    Servicio principal de la aplicación.

    Las interfaces nunca deberían comunicarse
    directamente con EnterpriseEngine.
    """

    def __init__(self) -> None:

        self.engine = EnterpriseEngine()

    def analyze(
        self,
        file_path: str | Path,
    ) -> str:
        """
        Analiza un archivo y devuelve la ruta
        del dashboard generado.
        """

        return self.engine.analyze_file(file_path)