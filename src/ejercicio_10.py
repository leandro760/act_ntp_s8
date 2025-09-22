import requests
import pandas as pd
import json

def users_dataframe_api():
    try:
        response = requests.get('https://playground.mockoon.com/users')
        
        if response.status_code == 200:
            data = response.json()
            
            processed_data = []
            for item in data:
                if isinstance(item, str):
                    try:
                        parsed_item = json.loads(item.replace('\r\n', ''))
                        processed_data.append(parsed_item)
                    except json.JSONDecodeError:
                        continue
                elif isinstance(item, dict):
                    processed_data.append(item)
                else:
                    continue
        
            if not processed_data:
                print("Error: No se encontraron datos válidos para procesar")
                return None
       
            df = pd.DataFrame(processed_data)
            
            print("Primeras 5 filas del DataFrame:")
            print(df.head())

            print("\nInformación del DataFrame:")
            print(df.info())
            
            return df
        else:
            print(f"Error: Código de estado {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar a la API")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {str(e)}")
        return None
    except ValueError as e:
        print(f"Error al procesar JSON: {str(e)}")
        return None

users_dataframe_api()




