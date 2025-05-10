¿Qué hace?
Tomas un fragmento de código y el sistema usa una pila para detectar errores como paréntesis mal cerrados, y una IA que te explica el error en lenguaje humano.

Innovación:
Combinas análisis estructural tradicional (pila) con una explicación generada por IA tipo “Te falta cerrar una llave en la línea 3”.

Herramientas sugeridas:

Python para análisis con pila

IA: OpenAI GPT o LLaMA para explicación

Verificas si la cima de la pila es el símbolo de apertura correspondiente.

Si coincide, haces un pop (sacas ese símbolo de la pila).

Si no coincide (o la pila está vacía), hay un error de estructura.
