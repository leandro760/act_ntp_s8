import pandas as pd

def productos():

    datos_productos = {
        "Producto": ["Laptop", "Smartphone", "Tablet"],
        "Precio": [2000000, 1500000, 800000],
        "Categoria": ["Computadores", "Telefonos", "Tablets"] 
    }

    df = pd.DataFrame(datos_productos)

    print("DataFrame Completo:")
    print(df)
    print("\nColumna Precio:")
    print(df['Precio'])
    print("\nInformación del DataFrame:")
    df.info()

productos()
