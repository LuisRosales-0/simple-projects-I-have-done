#leer y comparar 2 archivos excel y decir que litros no concuerdan entre uno y otro 

#se importan las librerias
import pandas as pd
import numpy as np

#cargamos los archivos
file1 = pd.read_excel('archivo1.xlsx')
file2 = pd.read_excel('archivo2.xls')

#cargamos los datos que se van a comparar
dt1 = (file1['Vol']).astype(float)
#print(dt1) 
dt2 = (file2['Lit']).astype(float)
#print(dt2) 

#funcion para encontrar y mostrar los litros que son iguales
for a in range(len(dt1)): #se define la longitud de las iteraciones utilizando como referencia el numero de filas que contiene nuestro archivo
    if np.array_equal(dt1.values[a],dt2.values[a]): #funcion de numpy para comparar en el arreglo si son iguales los valores del archivo
        print("Valores iguales en", a+1) #+1 puesto que en excel empieza con 1 y la iteracion parte del 0
        print(dt1.values[a])
        print(dt2.values[a])
        #se imprimen los valores
        print("") #solo es para hacer un salto de linea

print ('---------------------------')

#funcion para encontrar y mostrar los litros que NO son iguales
for i in range(len(dt1)): #de igual forma se define la longitud de las iteraciones utilizando como referencia el numero de filas que contiene nuestro archivo
    if not np.array_equal(dt1.values[i], dt2.values[i]): #en este caso el "not" nos sirve para decir comparar si NO son iguales los valores dentro del arreglo
        print("Valores no iguales en", i+1) #de igual forma el +1 ya que en excel empieza en 1 y la iteracion parte del 0
        print("dt1:", dt1.values[i])
        print("dt2:", dt2.values[i])
        #se imprimen los valores
        print("") #solo es para hacer un salto de linea






