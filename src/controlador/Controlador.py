from src.modelo.ejercicios.Ejercicio1 import *
from src.modelo.ejercicios.Ejercicio2 import *
from src.modelo.ejercicios.Ejercicio3 import *
from src.modelo.ejercicios.Ejercicio4 import *
from src.modelo.ejercicios.Ejercicio5 import *

from src.modelo.conexion.SparkSession import *
from src.modelo.conexion.ConexionJDBC import *

def ejecutar():
    df, spark_session = crear_sesion()
    conexion = ConexionJDBC()

    conexion.guardar_dataframe(df, "Datos2024", "overwrite")

    # Ejercicio 1a
    df = ejercicio_1a(df)

    # Ejercicio 1b
    df = ejercicio_1b(df)

    # Ejercicio 1c
    df = ejercicio_1c(df, spark_session)

    # Ejercicio 2a
    df = ejercicio_2a(df)

    # Ejercicio 2b
    ejercicio_2b(df)

    df = ejercicio3(df)

    ejercicio4(df)

    df = ejercicio5(df)

    conexion.guardar_dataframe(
        df,
        "Datos2024Tratados",
        "overwrite"
    )

