from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

# Ej2-a: Eliminar columnas y filas duplicadas. Cuantas se han eliminado
# Mostrar el count restante

def ejercicio_2a(df):
    filas_antes = df.count()

    df = df.dropDuplicates()
    filas_despues = df.count()

    df.show(7)
    filas_eliminadas = filas_antes - filas_despues

    print(f'Filas eliminadas: {filas_eliminadas}')
    print(f'Filas restantes: {filas_despues}')

    columnas_antes = len(df.columns)
    for c in df.columns:
        df_count = df.filter(col(c).isNull())
        if df_count.count() == df.count():
            df = df.drop(c)

    columnas_despues = len(df.columns)
    columnas_eliminadas = columnas_antes - columnas_despues

    print(f'Columnas eliminadas: {columnas_eliminadas}')
    print(f'Columnas restantes: {columnas_despues}')

    return df


# Ej2-b: Periodo temporal que cubren los datos y cuantos dias hay
# En este ejercicio se ha aplicado el uso de la IA porque usando head(1)[0] me daba error

def ejercicio_2b(df):
    fecha_min = df.agg(min("Fecha"))
    fecha_max = df.agg(max("Fecha"))

    fecha_min.show()
    fecha_max.show()

    total_dias = fecha_max.head(1)[0][0]- fecha_min.head(1)[0][0]
    print(total_dias)

    print("El total de días es cercano a un año pero faltan 2 días para completarlo.")
    print("No tiene sentido hacer un análisis de datos anual y sacar el primer y último día del año")