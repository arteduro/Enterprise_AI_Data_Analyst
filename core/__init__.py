"""
=========================================================
Enterprise AI Data Analyst (EADA)
---------------------------------------------------------
Paquete principal del núcleo (Core).

Este paquete contiene los componentes fundamentales del
sistema:

- Configuración global
- Logging
- Base de datos
- Gestión de proyectos
- Pipeline principal
- Excepciones personalizadas

Todos los módulos del proyecto dependen de este paquete.

Autor: Edgar Arteaga
Proyecto: Enterprise AI Data Analyst
Versión: 3.0.0
=========================================================
"""

__version__ = "3.0.0"
__author__ = "Edgar Arteaga"
__license__ = "MIT"

from .settings import Settings
from .logger import LoggerManager
from .database import DatabaseManager
from .project_manager import ProjectManager

__all__ = [
    "Settings",
    "LoggerManager",
    "DatabaseManager",
    "ProjectManager",
]
