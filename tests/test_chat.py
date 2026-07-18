"""
tests/test_chat.py

Prueba del Chat con el Dataset.

Autor: Edgar Arteaga
"""

from core.application.application_service import ApplicationService


def main():

    app = ApplicationService()

    app.analyze("datasets/ventas.xlsx")

    preguntas = [

        "¿Cuántas filas tiene el dataset?",

        "¿Cuántas columnas tiene?",

        "¿Cuántos valores nulos existen?",

        "¿Cuál es el promedio de Ventas?",

        "¿Cuál es el máximo de Ventas?",

        "¿Cuál es el promedio de Utilidad?",

        "¿Cuál es el máximo de Margen?",

        "¿Cuáles son las variables numéricas?"

    ]

    for pregunta in preguntas:

        print("=" * 70)

        print(pregunta)

        print()

        print(app.ask(pregunta))

        print()


if __name__ == "__main__":

    main()