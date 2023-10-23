import pulp
# Aqui se muestran los datos del ejercicio que se van a utilizar en el programa: Rendimientos Históricos de la moneda, Volatilidades de la moneda, y restricción de volatilidad máxima con la que se va a trabajar.
acciones = ["A", "B", "C", "D"]
rendimientos = [0.12, 0.15, 0.10, 0.09]
volatilidades = [0.18, 0.23, 0.15, 0.14]
volatilidad_maxima = 0.2
# Ahora procederemos a crear un problema de maximización.
problema = pulp.LpProblem("Optimización de Cartera", pulp.LpMaximize)
# Luego, comenzamos a definir las variables de decisión del problema (El peso de cada de las acciones en el problema).
pesos = pulp.LpVariable.dict("Peso", acciones, lowBound=0, upBound=1, cat="Continuous")
# Se continua definiendo la función objetivo en el programa (El rendimiento esperado de la cartera de monedas).
problema += pulp.lpSum(pesos[a] * rendimientos[i] for i, a in enumerate(acciones))
# Aqui se tiene la restricción de volatilidad máxima con la que se va a trabajar.
problema += pulp.lpSum(volatilidades[i] * pesos[accion] for i, accion in enumerate(acciones)) <= volatilidad_maxima
# Y aqui se tiene tambien la restricción de que la suma de los pesos tiene que ser igual a 1.
problema += pulp.lpSum(pesos[a] for a in acciones) == 1
# Y ahora, procedemos a resolver el problema del ejercicio.
problema.solve()
# Y por ultimo, se procede a mostrar los resultados del ejercicio realizado.
if pulp.LpStatus[problema.status] == "Optimal":
    for a in acciones:
        print(f"Asignación de peso para {a}: {pulp.value(pesos[a])}")
    rendimiento_optimo = pulp.value(problema.objective)
    print(f"Rendimiento esperado de la cartera optimizada: {rendimiento_optimo}")
else:
    print("No se encontró una solución óptima.")