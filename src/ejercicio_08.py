import json
import pandas as pd

def archivo_vehiculos_json():

    vehiculos = [
        {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2019},
        {'marca': 'Honda', 'modelo': 'Civic', 'año': 2020},
        {'marca': 'Ford', 'modelo': 'Focus', 'año': 2018}
    ]
    
    with open('vehiculos.json', mode='w', newline='', encoding='utf-8') as file:
            json.dump(vehiculos, file, indent=4)
            

    df = pd.read_json('vehiculos.json')

    print("DataFrame resultante:")
    print(df)

    print("\nTipos de datos:")
    print(df.dtypes)

archivo_vehiculos_json()


            