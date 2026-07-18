# 📜 Changelog

Todos los cambios importantes del proyecto **Enterprise AI Data Analyst** serán documentados en este archivo.

Este proyecto sigue un esquema de versionado basado en hitos de desarrollo y en los principios de **Semantic Versioning (SemVer)**.

---

# [0.3.0] - 2026-07-17

## 🚀 Añadido

- Nuevo proveedor **MockLLM** para desarrollo local sin consumir cuota de Gemini.
- Integración de **LLMFactory** para desacoplar el proveedor de modelos de IA.
- Infraestructura preparada para soportar múltiples proveedores LLM:
  - Google Gemini
  - OpenAI
  - Azure OpenAI
  - Anthropic
  - Ollama
- Primer sistema de caché para el análisis completo del dataset en Streamlit.

## ⚡ Mejorado

- Optimización importante en la generación de gráficos Plotly.
- Reducción del tiempo de renderizado del dashboard.
- Organización de las visualizaciones mediante pestañas.
- Actualización de la interfaz para utilizar la nueva API de Streamlit (`width="stretch"`).
- Mejor experiencia de usuario durante el análisis de datasets.

## 🔧 Refactorización

- Eliminadas las dependencias directas de `GeminiClient`.
- El motor de IA ahora obtiene el proveedor mediante `LLMFactory`.
- Separación de responsabilidades entre el motor analítico y los proveedores LLM.
- Optimización del flujo interno de generación de visualizaciones.

---

# [0.2.x]

## 🚀 Añadido

- Enterprise Engine.
- Application Service.
- Data Processor.
- Document Loader.
- AI Report Engine.
- Plotly Engine.
- Visualization Engine.
- Dashboard HTML.
- Pipeline completo de análisis.
- Integración con Google Gemini.
- Modelo `AnalysisResult` para separar el análisis del renderizado.

## ⚡ Mejorado

- Recuperación automática cuando Gemini no está disponible.
- Separación entre lógica de negocio e interfaz.
- Mejor organización de la arquitectura interna.

---

# [0.1.0]

## 🚀 Añadido

- Arquitectura inicial del proyecto.
- Organización modular.
- Configuración Git.
- README profesional.
- pyproject.toml.
- requirements.txt.
- .env.example.
- LICENSE.
- .gitignore.
- Base del proyecto Enterprise AI Data Analyst.