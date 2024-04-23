# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "Luciano", "Labudia", "Lolo", 33
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
"""
name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
print(name)
print(age)
"""

# Cambiamos su tipo
name = 35
age = "Luciano"
print(name)
print(age)

# Forzamos el tipo???
address: str = "Mi direccion"
address = True
address = 32
address = 1.5
print(type(address))