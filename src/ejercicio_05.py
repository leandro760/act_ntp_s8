import pandas as pd

def empleados():

    lista_empleados = [ {"empleado": "Zoe", "salario": 2500000, "departamento": "Ventas"},
                        {"empleado": "Pedro", "salario": 5000000, "departamento": "Almacen"},
                        {"empleado": "Juan", "salario": 3000000, "departamento": "Calidad"},
                        {"empleado": "Johana", "salario": 1800000, "departamento": "Almacen"}]
    
    df = pd.DataFrame(lista_empleados)


    print("Listado empleados:")
    print(df)
    print("\nEmpleado 2:")
    print(df.iloc[1])
    print("\nEmpleado 4:")
    print(df.iloc[3])

empleados()
    

