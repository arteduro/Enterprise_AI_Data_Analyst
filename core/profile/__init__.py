"""
core/profile/__init__.py

Módulo de perfilado del dataset.

Autor: Edgar Arteaga
"""

from .dataset_profile import DatasetProfile
from .profiler import DatasetProfiler

__all__ = [
    "DatasetProfile",
    "DatasetProfiler",
]