"""
config/logging_config.py

Configuración centralizada del sistema de logging.

Autor: Edgar Arteaga
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# ==========================================
# Directorio de logs
# ==========================================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "enterprise_ai.log"

# ==========================================
# Configuración única del logger
# ==========================================

_configured = False


def _configure_logging():
    """
    Configura el sistema de logging una única vez.
    """

    global _configured

    if _configured:
        return

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    root = logging.getLogger()

    root.setLevel(logging.INFO)

    root.handlers.clear()

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    root.addHandler(file_handler)

    root.addHandler(console_handler)

    _configured = True


def get_logger(name: str) -> logging.Logger:
    """
    Devuelve un logger configurado para cualquier módulo.
    """

    _configure_logging()

    return logging.getLogger(name)