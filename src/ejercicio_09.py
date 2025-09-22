import pandas as pd
import numpy as np

def ventas_trimestrales():

    datos_ventas = np.array([
                             [500000, 600000, 700000],
                             [550000, 650000, 750000],
                             [400000, 700000, 800000]
    ])

    df = pd.DataFrame(datos_ventas, columns=["Q1", "Q2", "Q3"])

    print("Ventas por trimestre:")
    print(df)

    print("\nTipos de datos:")
    print(df.dtypes)

ventas_trimestrales()