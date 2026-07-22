"""
Semantic Context Selector

Selecciona automáticamente las columnas
relevantes según la intención de la pregunta.

Autor: Edgar Arteaga
"""

from __future__ import annotations


class SemanticContextSelector:

    COLUMN_GROUPS = {

        "rentabilidad": [
            "Ventas",
            "Costo",
            "Costo Unitario",
            "Utilidad",
            "Margen",
            "Descuento",
        ],

        "ventas": [
            "Ventas",
            "Cantidad",
            "Precio Unitario",
            "Producto",
            "Categoría",
        ],

        "clientes": [
            "Cliente",
            "Segmento",
            "Ciudad",
            "Región",
            "Ventas",
        ],

        "productos": [
            "Producto",
            "Categoría",
            "Costo Unitario",
            "Precio Unitario",
            "Ventas",
        ],

        "regiones": [
            "Región",
            "Ciudad",
            "Ventas",
            "Utilidad",
        ],
    }

    def select_columns(
        self,
        question: str,
        dataframe,
    ) -> str:

        question = question.lower()

        selected = []

        for keyword, columns in self.COLUMN_GROUPS.items():

            if keyword in question:

                selected.extend(columns)

        if not selected:

            return ", ".join(dataframe.columns[:8])

        available = []

        for col in dataframe.columns:

            if col in selected:

                available.append(col)

        if not available:

            available = list(dataframe.columns[:8])

        return ", ".join(available)
