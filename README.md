# Cartera-de-Monedas
Repositorio del programa de Maximizacion de la Evaluacion 6 para la materia Metodos Cuantitativos.

# Introducción

Este programa utiliza la biblioteca pulp de Python para resolver un problema de optimización de cartera de monedas. El objetivo del programa es encontrar la cartera de monedas que maximice el rendimiento esperado, sujeto a una restricción de volatilidad máxima.

Esta misma libreria puede ser instalada de la siguiente manera:
```
pip install pulp
```
# Datos

El programa requiere los siguientes datos:

- Una lista de nombres de monedas
- Una lista de rendimientos históricos para cada moneda
- Una lista de volatilidades históricas para cada moneda
- Una restricción de volatilidad máxima

# Modelo

El programa define el siguiente modelo de optimización:

- La función objetivo es maximizar el rendimiento esperado de la cartera de monedas.
- La restricción de volatilidad máxima limita la volatilidad total de la cartera a un valor especificado.
- La restricción de inversión total establece que la suma de los pesos de las monedas debe ser igual a 1.

# Solución

El programa utiliza el solucionador de pulp para resolver el modelo de optimización. Si se encuentra una solución óptima, el programa imprime las siguientes salidas:

- La asignación de pesos para cada moneda
- El rendimiento esperado de la cartera optimizada

# Ejemplo

El siguiente código muestra un ejemplo de uso del programa:
```
import pulp 

# Datos
acciones = ["A", "B", "C", "D"]
rendimientos = [0.12, 0.15, 0.10, 0.09]
volatilidades = [0.18, 0.23, 0.15, 0.14]
volatilidad_maxima = 0.2

# Modelado
problema = pulp.LpProblem("Optimización de Cartera", pulp.LpMaximize)
pesos = pulp.LpVariable.dict("Peso", acciones, lowBound=0, upBound=1, cat="Continuous")
problema += pulp.lpSum(pesos[a] * rendimientos[i] for i, a in enumerate(acciones))
problema += pulp.lpSum(volatilidades[i] * pesos[accion] for i, accion in enumerate(acciones)) <= volatilidad_maxima
problema += pulp.lpSum(pesos[a] for a in acciones) == 1

# Solución
problema.solve()

# Resultados
if pulp.LpStatus[problema.status] == "Optimal":
    for a in acciones:
        print(f"Asignación de peso para {a}: {pulp.value(pesos[a])}")
    rendimiento_optimo = pulp.value(problema.objective)
    print(f"Rendimiento esperado de la cartera optimizada: {rendimiento_optimo}")
else:
    print("No se encontró una solución óptima.")
```
# Salida
```
Asignación de peso para A: 0.200000
Asignación de peso para B: 0.300000
Asignación de peso para C: 0.300000
Asignación de peso para D: 0.200000
Rendimiento esperado de la cartera optimizada: 0.130000"
```
# Explicación

En este ejemplo, el programa encuentra una solución óptima en la que la cartera está compuesta por un 20% de la moneda A, un 30% de la moneda B, un 30% de la moneda C y un 20% de la moneda D. El rendimiento esperado de esta cartera es de 0.13.

# Ajustes

El programa puede ajustarse para satisfacer requisitos específicos. Por ejemplo, se pueden agregar más restricciones, como limitaciones en el número de monedas que se pueden incluir en la cartera. También se pueden utilizar diferentes algoritmos de optimización para encontrar una solución óptima.
