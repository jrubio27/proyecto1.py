#pedios al asuario rellenar los siguientes datos
x = int (input ('Ingresa el valor de x: '))
y = int (input ('Ingresa el valor de y: '))
#proporsion de valores a los cuadrantes
if x==0:
    print ('Eje Y')
if y==0:
    print ('Eje X')
if x>0 and y>0:
    print ('Cuadrante I')
if x<0 and y>0:
    print ('Cuadrante II')
if x<0 and y<0:
    print ('Cuadrante III')
if x>0 and y<0:
    print ('Cuadrante VI')
print ()