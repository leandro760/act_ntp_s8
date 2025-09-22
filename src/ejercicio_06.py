import pandas as pd

def libros():

    datos_libros = [[ "El principito", "Antoine de Saint-Exupéry", 1943 ],
                    ["Rayuela", "Julio Cortázar", 1963 ],
                    ["De mil maneras de ser feliz", "Mario Benedetti", 2000 ],
                    ["La tregua", "Mario Benedetti", 1960 ]]
    
    nombres_columnas = ['Titulo', 'Autor', 'Año']

    df = pd.DataFrame(datos_libros, columns=nombres_columnas)

    print("Listado de libros:")
    print(df)
    print("\nDimensiones del DataFrame:", df.shape)


libros()


    
