#Vamos aprender las variables

#Esta es una variable string
my_string_variable = "Esta es mi variable"
print(my_string_variable) 

#Esta es una variable INT
my_int_variable = 5
print(my_int_variable) 

#Esta es una variable BOOL
my_bool_variable = False
print(my_bool_variable)

#Se realiza el llamado a disferentes variables o bien concatenacion de variables en print 
print(my_string_variable,my_int_variable,my_bool_variable)

'''En este apartado se utilizan las variables y tambien la operacion STR() que se ocupa para 
Convertir un dato int a string '''
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Algunas Funciones del sistema
#LEN se utiliza para saber cuantos caracteres existen contando espacios 
print(len(my_string_variable))

#A los print tambien se le puede agregar textos predefinidos
print("Este es el valor de la variable:",my_int_variable)

#Variables en una sola linea ¡Cuidado con abusar con esta sintaxis !
name, surname, alias, age = "Walter ", "Ruyan", "Wruyans", 21
print("Mi nombres es:",name,"Mi apellido es:", surname, "Tengo",age,"Años", "Y mi alias es:", alias )

'''#Teclado en pantalla o input()
name = input("¿Cual es tu nombre?:")
age= input("¿Que edad tienes?:")
print(name)
print(age) '''

'Cambiamos su tipo'
name=32
age="Walter"
print(name)
print(age)
