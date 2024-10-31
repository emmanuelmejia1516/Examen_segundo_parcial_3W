print("Mejia_Suarez_Emmanuel_Alexander_1197_3W")
# Programa que almacena los créditos de las asignaturas y muestra el total

# Diccionario con asignaturas y sus créditos
creditos = {'Matemáticas': 6, 'ingles': 9, 'humanidades': 10}

# Mostrar créditos de cada asignatura
for asignatura, credito in creditos.items():
    print(f"{asignatura} tiene {credito} créditos.")

# Calcular y mostrar el total de créditos
total_creditos = sum(creditos.values())
print("El número total de créditos del curso es:", total_creditos)
