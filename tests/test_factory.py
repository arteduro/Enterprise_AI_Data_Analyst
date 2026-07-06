"""
tests/test_factory.py

Prueba del LLM Factory.

Autor: Edgar Arteaga
"""

from llm.llm_factory import LLMFactory


def main():

    llm = LLMFactory.create()

    print(type(llm).__name__)

    respuesta = llm.generate(
        "Di únicamente: Factory funcionando."
    )

    print("\n===== RESPUESTA =====\n")

    print(respuesta)


if __name__ == "__main__":
    main()