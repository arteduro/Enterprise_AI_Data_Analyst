"""
Configuración centralizada de logs.
Autor: Edgar Arteaga
"""

import logging
from pathlib import Path

# ===========================
# Carpeta de logs
# ===========================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "enterprise_ai.log"

# ===========================
# Configuración
# ===========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("EnterpriseAI")