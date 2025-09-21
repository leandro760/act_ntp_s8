import pandas as pd

def analisis_ventas_diarias():

    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165])
                                
    indice_3 = ventas[3]
    promedio_ventas = ventas.mean()
    ventas_ordenadas = ventas.sort_values()

    print("Ventas diarias:\n")
    print(ventas)
    print("\nValor en el índice 3:", indice_3 )
    print("\nPromedio de ventas:", promedio_ventas)
    print("\nVentas ordenadas:\n")
    print(ventas_ordenadas)

analisis_ventas_diarias()
    