"""
core/project_manager.py
Gestor de proyectos del sistema.
"""
from pathlib import Path
from datetime import datetime
from .settings import settings
from .logger import LoggerManager

class ProjectManager:
    def __init__(self):
        settings.create_directories()
        self.logger=LoggerManager.get_logger("ProjectManager")
        self.root=Path(settings.PROJECTS_DIR)

    def create_project(self,name:str)->Path:
        safe=name.replace(" ","_")
        ts=datetime.now().strftime("%Y%m%d_%H%M%S")
        p=self.root/f"{safe}_{ts}"
        for sub in ["datasets","artifacts","reports","models","chat_history","logs"]:
            (p/sub).mkdir(parents=True,exist_ok=True)
        self.logger.info(f"Proyecto creado: {p}")
        return p

    def list_projects(self):
        return sorted([x for x in self.root.iterdir() if x.is_dir()])

    def delete_project(self,path:Path):
        import shutil
        shutil.rmtree(path,ignore_errors=True)
        self.logger.info(f"Proyecto eliminado: {path}")
