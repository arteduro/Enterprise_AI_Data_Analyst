"""
core/engines/analysis_engine.py

Motor de análisis de Enterprise AI Data Analyst.

Orquesta la carga y el análisis de datasets.

Autor: Edgar Arteaga
"""

from __future__ import annotations

import pandas as pd

from config.logging_config import get_logger

from core.data_processor import DataProcessor
from core.document_loader import DocumentLoader

logger = get_logger(__name__)


# ==========================================================
# Motor de análisis
# ==========================================================


class AnalysisEngine:
    """
    Orquesta el flujo completo de análisis
    de un dataset.

    Coordina la carga del archivo y el
    procesamiento del DataFrame.
    """

    def __init__(self) -> None:
        """
        Inicializa los componentes del motor.
        """

        self.loader = DocumentLoader()

        self.processor = DataProcessor()

    def analyze_dataframe(
        self,
        dataframe: pd.DataFrame,
    ):
        """
        Ejecuta el análisis completo de un DataFrame.
        """

        logger.info(
            "Iniciando análisis del DataFrame..."
        )

        result = self.processor.profile(
            dataframe
        )

        logger.info(
            "Análisis del DataFrame finalizado."
        )

        return result

    def analyze_file(
        self,
        file_path: str,
    ):
        """
        Carga un archivo y ejecuta
        el análisis completo.
        """

        logger.info(
            "Iniciando análisis del archivo..."
        )

        dataframe = self.loader.load(
            file_path
        )

        return self.analyze_dataframe(
            dataframe
        )