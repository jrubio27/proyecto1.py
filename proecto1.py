print("favor de rellenar los siguentes dato")
nombre = input("nombre completo porfavor ")
apellidop = input("apellido paterno ")
apellidom = input("apellido materno ")
edad = int(input("edad "))
peso = float(input("peso en kg "))
altura = float(input("altura en metros "))
imc = peso / altura**2
print(f"gracias, {nombre} {apellidop} {apellidom}. su imc es {imc:.2f}")
if imc >= 0 and imc <= 18.99 :
    print("peso bajo")
elif imc >= 19 and imc <= 24.99 :
    print ("peso normal")
elif imc >= 25 and imc <= 29.99 :
    print ("sobre peso")
elif imc >= 30 and imc <= 34.99 :
    print ("evesidad leve")
elif imc >= 35 and imc <= 39.99 :
    print("ebesidad media")
elif imc >= 40 :
    print ("obesidad morbida")
print (f"gracias por su tiempo que tenga un excelente dia")
