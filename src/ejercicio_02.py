import pandas as pd

def datos_calificaciones():

    calificaciones =  pd.Series([85, 92, 78], 
                                index=['Matemáticas', 'Ciencias', 'Historia'])
    
    ciencias = calificaciones['Ciencias']
    suma = calificaciones.sum()
    promedio = calificaciones.mean()

    print("Calificaciones:\n")
    print(calificaciones)
    print("\nCalificación en Ciencias:")
    print(ciencias)
    print("\nInformación basica de la serie:")
    print(calificaciones.describe())
    print("\nSuma de calificaciones:")  
    print(suma)
    print("\nPromedio de calificaciones:")
    print(promedio)

datos_calificaciones()
