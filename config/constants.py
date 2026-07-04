"""
Constantes globales de Enterprise AI Data Analyst.
Autor: Edgar Arteaga
"""

# ===========================
# Archivos soportados
# ===========================

SUPPORTED_FILE_TYPES = [
    ".csv",
    ".xlsx",
    ".xls",
    ".pdf",
    ".docx",
    ".txt",
    ".json",
    ".xml"
]

# ===========================
# Tamaños máximos
# ===========================

MAX_UPLOAD_SIZE_MB = 100

MAX_CHAT_HISTORY = 20

MAX_DATASET_ROWS = 1_000_000

# ===========================
# Idioma
# ===========================

DEFAULT_LANGUAGE = "es"

DEFAULT_ENCODING = "utf-8"

# ===========================
# IA
# ===========================

DEFAULT_TEMPERATURE = 0.2

DEFAULT_MAX_TOKENS = 8192

DEFAULT_TOP_P = 0.95

# ===========================
# Reportes
# ===========================

REPORTS_FOLDER = "reports"

PROJECTS_FOLDER = "projects"

UPLOAD_FOLDER = "uploads"

LOG_FOLDER = "logs"