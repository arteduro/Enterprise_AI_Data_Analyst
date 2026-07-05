"""
tests/test_gemini.py

Prueba de conexión con Google Gemini.
"""

from llm.gemini_client import GeminiClient


def main():
    client = GeminiClient()

    print("Verificando conexión con Gemini...")

    if client.health_check():

        print("[OK] Conexión exitosa")

        respuesta = client.generate(
            "Preséntate como Enterprise AI Data Analyst en máximo 3 líneas."
        )

        print("\n===== RESPUESTA =====\n")
        print(respuesta)

    else:

        print("[ERROR] No fue posible conectar con Gemini.")


if __name__ == "__main__":
    main()