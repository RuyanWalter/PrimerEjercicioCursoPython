##Vamos aprender los operadores Aritmeticos 
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

#Podemos concatenar dos cadenas de textos por medio del operador +

print("Hola " + "Python")

print("Hola " + "Python" + '¿Que tal?')

#Podemos concatenar y convertir un int en un string usando la funcion del sistema str()
print("Hola " + str(5)) 

#Vamos a multiplicar la palabra hola con el operador *
print("Hola " * 4) 
print("Hola " * (2 ** 4)) 

#Vamos a transformar un float a int 
my_float = 2.5 * 2 
print("Hola" * int(my_float))

"""
Este tipo de concatenacion con el simbolo - da error 
puesto queno todos los operadores se pueden utilizar 

print("Hola" - "Python")
print("Hola" + 5")

"""
### Operadores Comparativos 

print(3 > 4)
print(3 > 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

#Haremos las comparaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" > "Python")
print("Hola" <= "Python")
print("Hola" >= "Zola") # Ordenación Alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos 

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4 )) #Niega toda la condicion 
