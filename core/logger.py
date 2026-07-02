"""
core/logger.py
Sistema de logging centralizado.
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from .settings import settings

class LoggerManager:
    _configured=False

    @classmethod
    def get_logger(cls,name:str)->logging.Logger:
        if not cls._configured:
            settings.create_directories()
            log_file=Path(settings.LOGS_DIR)/"enterprise_ai.log"
            fmt=logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
            root=logging.getLogger()
            root.setLevel(logging.INFO)
            fh=RotatingFileHandler(log_file,maxBytes=5*1024*1024,backupCount=5,encoding="utf-8")
            fh.setFormatter(fmt)
            sh=logging.StreamHandler()
            sh.setFormatter(fmt)
            root.handlers.clear()
            root.addHandler(fh)
            root.addHandler(sh)
            cls._configured=True
        return logging.getLogger(name)
