import pandas as pd 

def operaciones_series():
    
    precios = pd.Series([100, 150, 200], 
                        index=['Yuca', 'Banano', 'Fresa'])
    descuentos = pd.Series([10, 20, 15], 
                        index=['Yuca', 'Banano', 'Fresa'])
    
    precios_con_descuento = precios - descuentos
    
    precios_con_iva = precios * 1.16
    
    print("Precios originales:")
    print(precios)
    print("\nDescuentos:")
    print(descuentos)
    print("\nPrecios con descuento de cada producto:")
    print(precios_con_descuento)
    print("\nPrecios con IVA de cada producto:")
    print(precios_con_iva)

operaciones_series()

    