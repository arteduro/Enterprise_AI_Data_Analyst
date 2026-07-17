"""
scripts/generate_dataset.py

Generador de datasets empresariales para
Enterprise AI Data Analyst.

Autor: Edgar Arteaga
"""

from pathlib import Path
from random import choice, randint, uniform

import pandas as pd

# --------------------------------------------------------
# Configuración
# --------------------------------------------------------

TOTAL_REGISTROS = 1000

OUTPUT = Path("datasets/ventas.xlsx")

CIUDADES = [
    "Bogotá",
    "Medellín",
    "Cali",
    "Barranquilla",
    "Cúcuta",
    "Bucaramanga",
    "Pereira",
    "Cartagena",
]

REGIONES = {
    "Bogotá": "Centro",
    "Medellín": "Antioquia",
    "Cali": "Pacífico",
    "Barranquilla": "Caribe",
    "Cúcuta": "Oriente",
    "Bucaramanga": "Oriente",
    "Pereira": "Eje Cafetero",
    "Cartagena": "Caribe",
}

PRODUCTOS = [
    "Laptop",
    "Monitor",
    "Teclado",
    "Mouse",
    "Servidor",
    "Router",
    "Tablet",
    "Impresora",
]

CATEGORIAS = {
    "Laptop": "Computo",
    "Monitor": "Computo",
    "Teclado": "Accesorios",
    "Mouse": "Accesorios",
    "Servidor": "Infraestructura",
    "Router": "Networking",
    "Tablet": "Movilidad",
    "Impresora": "Periféricos",
}

SEGMENTOS = [
    "Retail",
    "Empresarial",
    "Gobierno",
]

CANALES = [
    "Online",
    "Tienda",
    "Distribuidor",
]

ESTADOS = [
    "Completada",
    "Pendiente",
    "Cancelada",
]

VENDEDORES = [
    "Laura",
    "Carlos",
    "Andrés",
    "Paula",
    "Sofía",
    "Camilo",
    "Juliana",
    "Miguel",
]

# --------------------------------------------------------

fechas = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
)

rows = []

for i in range(TOTAL_REGISTROS):

    ciudad = choice(CIUDADES)

    producto = choice(PRODUCTOS)

    precio = randint(50, 8000)

    costo = precio * uniform(0.45, 0.80)

    cantidad = randint(1, 20)

    descuento = round(uniform(0, 0.20), 2)

    venta = precio * cantidad * (1 - descuento)

    costo_total = costo * cantidad

    utilidad = venta - costo_total

    margen = utilidad / venta if venta else 0

    rows.append(
        {
            "Fecha": choice(fechas),
            "Ciudad": ciudad,
            "Región": REGIONES[ciudad],
            "Cliente": f"Cliente {randint(1,250)}",
            "Segmento": choice(SEGMENTOS),
            "Producto": producto,
            "Categoría": CATEGORIAS[producto],
            "Cantidad": cantidad,
            "Precio Unitario": round(precio, 2),
            "Costo Unitario": round(costo, 2),
            "Descuento": descuento,
            "Ventas": round(venta, 2),
            "Costos": round(costo_total, 2),
            "Utilidad": round(utilidad, 2),
            "Margen": round(margen * 100, 2),
            "Vendedor": choice(VENDEDORES),
            "Canal": choice(CANALES),
            "Estado": choice(ESTADOS),
        }
    )

df = pd.DataFrame(rows)

OUTPUT.parent.mkdir(exist_ok=True)

df.to_excel(
    OUTPUT,
    index=False,
)

print("=" * 60)
print("DATASET GENERADO")
print("=" * 60)
print()
print(f"Archivo : {OUTPUT}")
print(f"Registros : {len(df):,}")
print(f"Columnas : {len(df.columns)}")
print()
print(df.head())