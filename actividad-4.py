print("Mejia_Suarez_Emmanuel_Alexander_1197_3W")
# Programa que almacena datos personales en un diccionario

# Diccionario para almacenar los datos del usuario
datos_usuario = {}

# Preguntar los datos al usuario
datos_usuario['nombre'] = input("¿Cuál es tu nombre? ")
datos_usuario['edad'] = input("¿Cuál es tu edad? ")
datos_usuario['dirección'] = input("¿Cuál es tu dirección? ")
datos_usuario['teléfono'] = input("¿Cuál es tu número de teléfono? ")

# Mostrar los datos del usuario
print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['dirección']} y su número de teléfono es {datos_usuario['teléfono']}.")
