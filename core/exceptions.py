"""
core/exceptions.py

Excepciones personalizadas para Enterprise AI Data Analyst.
"""

class EADAError(Exception):
    """Excepción base del proyecto."""
    pass

class ConfigurationError(EADAError):
    """Error en la configuración del sistema."""
    pass

class DatabaseError(EADAError):
    """Error relacionado con la base de datos."""
    pass

class ProjectError(EADAError):
    """Error en la gestión de proyectos."""
    pass

class DatasetError(EADAError):
    """Error al cargar o procesar un dataset."""
    pass

class DatasetNotFoundError(DatasetError):
    """No se encontró el dataset solicitado."""
    pass

class InvalidDatasetFormatError(DatasetError):
    """Formato de dataset no soportado."""
    pass

class RAGError(EADAError):
    """Error en el motor RAG."""
    pass

class EmbeddingError(RAGError):
    """Error al generar embeddings."""
    pass

class AutoMLError(EADAError):
    """Error durante el proceso AutoML."""
    pass

class ModelTrainingError(AutoMLError):
    """Error al entrenar un modelo."""
    pass

class PredictionError(AutoMLError):
    """Error al realizar predicciones."""
    pass

class DashboardError(EADAError):
    """Error al generar el dashboard."""
    pass

class ReportError(EADAError):
    """Error al generar reportes."""
    pass

class ChatError(EADAError):
    """Error en el módulo de chat."""
    pass

class MemoryError(EADAError):
    """Error en el sistema de memoria."""
    pass
