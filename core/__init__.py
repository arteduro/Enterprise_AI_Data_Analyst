"""
=========================================================
Enterprise AI Data Analyst (EADA)
---------------------------------------------------------
Paquete principal del núcleo (Core).

Este paquete contiene los componentes fundamentales del
sistema.

Autor: Edgar Arteaga
Versión: 3.0.0
=========================================================
"""

__version__ = "3.0.0"
__author__ = "Edgar Arteaga"
__license__ = "MIT"

from .database import DatabaseManager
from .logger import LoggerManager
from .project_manager import ProjectManager
from .settings import Settings

__all__ = [
    "Settings",
    "LoggerManager",
    "DatabaseManager",
    "ProjectManager",
]