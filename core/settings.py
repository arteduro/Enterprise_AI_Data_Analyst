"""
core/settings.py
Configuración central del proyecto Enterprise AI Data Analyst.
"""

from pathlib import Path
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    PROJECT_NAME: str = "Enterprise AI Data Analyst"
    VERSION: str = "3.0.0"

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    CORE_DIR: Path = BASE_DIR / "core"
    AGENTS_DIR: Path = BASE_DIR / "agents"
    AUTOML_DIR: Path = BASE_DIR / "automl"
    RAG_DIR: Path = BASE_DIR / "rag"
    MEMORY_DIR: Path = BASE_DIR / "memory"
    DASHBOARD_DIR: Path = BASE_DIR / "dashboard"
    REPORTS_DIR: Path = BASE_DIR / "reports"
    DATABASE_DIR: Path = BASE_DIR / "database"
    ARTIFACTS_DIR: Path = BASE_DIR / "artifacts"
    PROJECTS_DIR: Path = BASE_DIR / "projects"
    UPLOADS_DIR: Path = BASE_DIR / "uploads"
    LOGS_DIR: Path = BASE_DIR / "logs"

    SQLITE_PATH: Path = DATABASE_DIR / "enterprise_ai.db"

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    LANGSMITH_API_KEY: str = os.getenv("LANGSMITH_API_KEY", "")

    DEFAULT_MODEL: str = "gemini-2.5-pro"
    EMBEDDING_MODEL: str = "text-embedding-004"

    DEBUG: bool = True

    @classmethod
    def create_directories(cls):
        for d in [
            cls.AGENTS_DIR, cls.AUTOML_DIR, cls.RAG_DIR,
            cls.MEMORY_DIR, cls.DASHBOARD_DIR, cls.REPORTS_DIR,
            cls.DATABASE_DIR, cls.ARTIFACTS_DIR,
            cls.PROJECTS_DIR, cls.UPLOADS_DIR, cls.LOGS_DIR
        ]:
            d.mkdir(parents=True, exist_ok=True)

settings = Settings()
