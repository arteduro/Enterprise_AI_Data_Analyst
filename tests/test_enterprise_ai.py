"""
Prueba del núcleo EnterpriseAI.
"""

from core.enterprise_ai import EnterpriseAI


def main():

    ai = EnterpriseAI()

    print("===== Enterprise AI =====")

    if ai.health_check():

        print("[OK] Sistema operativo")

    respuesta = ai.ask(
        "Responde únicamente: EnterpriseAI funcionando."
    )

    print("\n===== RESPUESTA =====\n")

    print(respuesta)


if __name__ == "__main__":
    main()