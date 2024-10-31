print("Mejia_Suarez_Emmanuel_Alexander_1197_3W")
# Programa que almacena las asignaturas y muestra las notas obtenidas

# Lista de asignaturas
asignaturas = ["Matemáticas", "ecosistemas", "humanidades", "metodologias", "Lengua y comunicacion", "ingles"]

# Diccionario para almacenar las notas
notas = {}

# Preguntar la nota en cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    notas[asignatura] = nota

# Mostrar las notas obtenidas
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}.")
