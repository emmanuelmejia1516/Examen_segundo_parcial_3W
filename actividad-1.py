print("Mejia_Suarez_Emmanuel_Alexander_1197_3W")
# Programa que almacena las asignaturas de un curso y elimina las aprobadas

# Lista de asignaturas
asignaturas = ["Matemáticas", "ecosistemas", "humanidades", "metodologias", "Lengua y comunicacion", "ingles"]

# Notas aprobadas
asignaturas_a_repetir = []

# Preguntar la nota en cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota < 6:  # Consideramos que la nota mínima para aprobar es 6
        asignaturas_a_repetir.append(asignatura)

# Mostrar las asignaturas que se deben repetir
print("Las asignaturas que tienes que repetir son:", asignaturas_a_repetir)