"""
Configuración global de Enterprise AI Data Analyst

Autor: Edgar Arteaga
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# ==============================
# Cargar variables de entorno
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# ==============================
# Configuración principal
# ==============================


class Settings:

    # --------------------------
    # Proyecto
    # --------------------------

    PROJECT_NAME = "Enterprise AI Data Analyst"

    VERSION = "0.1.0"

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "True"
    ) == "True"

    # --------------------------
    # Proveedor de IA
    # --------------------------

    MODEL_PROVIDER = os.getenv(
        "MODEL_PROVIDER",
        "google"
    )

    # --------------------------
    # Gemini
    # --------------------------

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    THINKING_LEVEL = os.getenv(
        "THINKING_LEVEL",
        "high"
    )

    TEMPERATURE = float(
        os.getenv(
            "TEMPERATURE",
            0.2
        )
    )

    MAX_OUTPUT_TOKENS = int(
        os.getenv(
            "MAX_OUTPUT_TOKENS",
            8192
        )
    )

    # --------------------------
    # LangSmith
    # --------------------------

    LANGSMITH_API_KEY = os.getenv(
        "LANGSMITH_API_KEY"
    )

    LANGSMITH_TRACING = os.getenv(
        "LANGSMITH_TRACING",
        "true"
    )

    PROJECT_TRACE_NAME = os.getenv(
        "PROJECT_TRACE_NAME",
        PROJECT_NAME
    )


settings = Settings()