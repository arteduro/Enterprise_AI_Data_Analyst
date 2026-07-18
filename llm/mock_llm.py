"""
llm/mock_llm.py

Proveedor simulado para desarrollo.

No consume llamadas a Gemini.

Autor: Edgar Arteaga
"""

from typing import Optional

from llm.base_llm import BaseLLM


class MockLLM(BaseLLM):
    """
    Simula un proveedor LLM.
    """

    def generate(
        self,
        prompt: str,
        context: Optional[str] = None,
    ) -> str:

        return """
# Resumen Ejecutivo

El conjunto de datos fue analizado correctamente.

## Hallazgos Importantes

- El dataset presenta una estructura consistente.
- No se detectaron errores críticos.
- La calidad general de los datos es adecuada para análisis.

## Riesgos Detectados

- No se identifican riesgos importantes.
- Se recomienda validar periódicamente la calidad de los datos.

## Recomendaciones

- Continuar con el análisis exploratorio.
- Construir modelos predictivos utilizando las variables relevantes.
- Monitorear posibles cambios en la distribución de los datos.

## Próximos Pasos

1. Analizar correlaciones.
2. Evaluar variables objetivo.
3. Entrenar modelos de Machine Learning.
4. Generar dashboard ejecutivo.

---
**MockLLM**
Informe generado localmente (sin consumir Gemini).
""".strip()

    def health_check(self) -> bool:
        return True