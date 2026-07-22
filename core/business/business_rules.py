"""
core/business/business_rules.py

Enterprise Business Rules Engine

Detecta automáticamente el dominio de negocio
a partir de los nombres de columnas.

Autor: Edgar Arteaga
"""

from __future__ import annotations


class BusinessRules:

    """
    Descubre reglas empresariales
    utilizando los nombres de columnas.
    """

    # ==========================================
    # DICCIONARIO
    # ==========================================

    RULES = {

        # Comercial

        "venta": "Indicador Comercial",

        "ventas": "Indicador Comercial",

        "cliente": "Entidad Comercial",

        "clientes": "Entidad Comercial",

        "producto": "Catálogo Comercial",

        "productos": "Catálogo Comercial",

        "cantidad": "Volumen Comercial",

        "precio": "Precio de Venta",

        # Financiero

        "utilidad": "Indicador Financiero",

        "ganancia": "Indicador Financiero",

        "margen": "Rentabilidad",

        "costo": "Costo Operacional",

        "costos": "Costo Operacional",

        "ingreso": "Ingresos",

        "ingresos": "Ingresos",

        # Tiempo

        "fecha": "Variable Temporal",

        "mes": "Variable Temporal",

        "año": "Variable Temporal",

        "anio": "Variable Temporal",

        "dia": "Variable Temporal",

        # Inventario

        "stock": "Inventario",

        "inventario": "Inventario",

        "existencia": "Inventario",

        # Geografía

        "ciudad": "Ubicación",

        "pais": "Ubicación",

        "departamento": "Ubicación",

        "region": "Ubicación",

    }

    # ==========================================
    # ANALIZAR COLUMNAS
    # ==========================================

    def analyze(
        self,
        columns: list[str],
    ) -> list[str]:

        rules = []

        for column in columns:

            lower = column.lower()

            for keyword, meaning in self.RULES.items():

                if keyword in lower:

                    rules.append(

                        f"{column}: {meaning}"

                    )

                    break

        return rules

    # ==========================================
    # TEXTO
    # ==========================================

    def build_text(
        self,
        columns: list[str],
    ) -> str:

        rules = self.analyze(columns)

        if not rules:

            return (
                "No se identificaron reglas empresariales."
            )

        return "\n".join(

            f"• {rule}"

            for rule in rules

        )