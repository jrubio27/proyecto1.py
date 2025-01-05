#identificar la logitud de una palabra
def verificar_longitud_palabra(palabra):
  longitud = len(palabra)
  if 4 <= longitud <= 8:
    return "La palabra es correcta."
  elif longitud < 4:
    return f"Hacen falta letras. Solo tiene {longitud} letras."
  else:
    return f"Sobran letras. Tiene {longitud} letras."
# Solicita al usuario ingresar una palabra
palabra = input("Ingrese una palabra: ")
# Llama a la función para verificar la longitud y muestra el resultado
resultado = verificar_longitud_palabra(palabra)
print(resultado)