"""
core/pipeline.py
Orquestador principal del sistema.
"""
from core.logger import LoggerManager
from core.project_manager import ProjectManager
from core.database import DatabaseManager

class Pipeline:
    def __init__(self):
        self.logger=LoggerManager.get_logger("Pipeline")
        self.pm=ProjectManager()
        self.db=DatabaseManager()

    def initialize(self):
        self.logger.info("Inicializando plataforma...")
        self.db.initialize()
        self.logger.info("Plataforma inicializada.")

    def create_project(self,name:str):
        return self.pm.create_project(name)

    def run(self,dataset_path:str):
        self.logger.info("="*60)
        self.logger.info("Inicio del Pipeline Enterprise AI Data Analyst")
        self.logger.info(f"Dataset: {dataset_path}")
        self.logger.info("Paso 1: Validación")
        self.logger.info("Paso 2: Preprocesamiento (pendiente)")
        self.logger.info("Paso 3: Memoria (pendiente)")
        self.logger.info("Paso 4: RAG (pendiente)")
        self.logger.info("Paso 5: Agentes IA (pendiente)")
        self.logger.info("Paso 6: AutoML (pendiente)")
        self.logger.info("Paso 7: Explicabilidad (pendiente)")
        self.logger.info("Paso 8: Dashboard (pendiente)")
        self.logger.info("Paso 9: Reportes (pendiente)")
        self.logger.info("Paso 10: Chat (pendiente)")
        self.logger.info("Pipeline finalizado.")
