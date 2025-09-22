import csv
import pandas as pd

def archivo_cursos_csv():

    cursos= [
        ['Curso', 'Instructor', 'Duracion'],
        ["Web II", "Carlos Gomez", "6 meses"],
        ["Moviles II", "Ana Perez", "5 meses"],
        ["Nuevas Tecnologias", "Luis Martinez", "4 meses"]
        ]
    
    try:

        with open('cursos.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(cursos)
            

        df = pd.read_csv('cursos.csv')

        print("DataFrame resultante:")
        print(df)

    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

archivo_cursos_csv()


            