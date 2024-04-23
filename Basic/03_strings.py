# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro string'
print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String \n con un salto de línea"
print(my_new_line_string)

my_tab_string = "Este es un String \t con un tabulador"
print(my_tab_string)

my_scaped_string = "\\tEste es un String \\n con un backslash"
print(my_scaped_string)

# Formateo

name, surname, age = "Luciano", "Labudia", 33

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) # Python
print(language.upper()) # PYTHON
print(language.count("t")) # 1
print(language.isnumeric()) # False
print("1".isnumeric()) # True
print(language.lower()) # python
print(language.lower().issupper()) # False
print(language.startswith("Py")) # True
print("Py" == "py")  # No es lo mismo




