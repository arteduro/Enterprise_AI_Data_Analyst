# 📜 Changelog

Todos los cambios importantes del proyecto **Enterprise AI Data Analyst** serán documentados en este archivo.

Este proyecto sigue un esquema de versionado basado en **Semantic Versioning (SemVer)**.

---

# [0.8.0] - 2026-07-19

## 🚀 Añadido

### 🧠 Enterprise AI Context Engine

- Nuevo motor inteligente de contexto para Gemini.
- Construcción automática de contexto antes de cada consulta.
- Integración del perfil completo del dataset dentro del prompt.
- Contexto enriquecido con:
  - Variables numéricas
  - Variables categóricas
  - Estadísticas descriptivas
  - Dataset Profile
  - Historial conversacional
  - Pregunta actual

### 💬 Memoria Conversacional

- Nuevo módulo `ConversationMemory`.
- Registro automático de:
  - preguntas del usuario
  - respuestas de la IA.
- Historial reutilizable entre consultas.
- Funciones para limpiar memoria.
- Preparado para persistencia futura.

### 📊 Dataset Profile

Nuevo sistema de perfil inteligente del dataset.

Incluye:

- Número de filas.
- Número de columnas.
- Variables numéricas.
- Variables categóricas.
- Valores nulos.
- Estadísticas descriptivas.
- Variables disponibles para la IA.
- Resumen ejecutivo del dataset.

### 🧩 Context Builder

Nuevo módulo encargado de construir el prompt completo para Gemini.

Combina automáticamente:

- Dataset Profile.
- Memoria conversacional.
- Contexto del análisis.
- Pregunta actual.

### 🧭 Router Inteligente

Se consolida el sistema de enrutamiento de consultas.

Rutas disponibles:

- Motor interno.
- Gemini.
- Híbrido (preparado para próximas versiones).

### 🤖 Integración IA

- Gemini ahora recibe contexto empresarial completo.
- Respuestas mucho más específicas.
- Menor alucinación del modelo.
- Mayor coherencia entre preguntas consecutivas.

---

## ⚡ Mejorado

- Mayor calidad de respuestas generadas por Gemini.
- El modelo ya conoce el dataset sin necesidad de repetir información.
- El chat mantiene continuidad entre preguntas.
- Mejor organización del flujo Application → Context → LLM.
- Preparación completa para RAG.

---

## 🔧 Refactorización

Se reorganizó la arquitectura del proyecto.

Nuevos paquetes:

```
core/context
core/memory
core/profile
core/services
core/routing
```

Se desacoplaron responsabilidades entre:

- ApplicationService
- ContextBuilder
- ConversationMemory
- DatasetProfile
- LLMService

La aplicación ahora sigue una arquitectura mucho más cercana a sistemas Enterprise AI modernos.

---

# [0.7.0] - 2026-07-19

## 🚀 Añadido

- Router Inteligente de IA.
- Integración oficial con Google Gemini.
- Nuevo `LLMService`.
- `ApplicationService` como punto único de entrada.
- Detección automática entre consultas internas y consultas IA.
- Mensaje amigable cuando la cuota gratuita de Gemini se encuentra agotada.

---

## ⚡ Mejorado

- Mejor separación entre reglas de negocio y comunicación con la IA.
- Arquitectura preparada para múltiples proveedores LLM.

---

# [0.3.0] - 2026-07-17

## 🚀 Añadido

- Nuevo proveedor **MockLLM** para desarrollo local.
- Integración de **LLMFactory**.
- Infraestructura preparada para múltiples proveedores:
  - Google Gemini
  - OpenAI
  - Azure OpenAI
  - Anthropic
  - Ollama
- Caché para análisis del dataset.

## ⚡ Mejorado

- Optimización del dashboard Plotly.
- Mejor rendimiento de Streamlit.
- Uso de pestañas.
- Adaptación a la nueva API de Streamlit.

## 🔧 Refactorización

- Eliminadas dependencias directas de Gemini.
- Separación entre motor analítico y proveedores LLM.

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
- Modelo `AnalysisResult`.

## ⚡ Mejorado

- Recuperación automática cuando Gemini no está disponible.
- Separación entre lógica de negocio e interfaz.

---

# [0.1.0]

## 🚀 Añadido

- Arquitectura inicial.
- Organización modular.
- README profesional.
- GitHub inicial.
- pyproject.toml.
- requirements.txt.
- .env.example.
- LICENSE.
- .gitignore.