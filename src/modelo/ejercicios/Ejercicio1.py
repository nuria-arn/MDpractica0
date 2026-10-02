from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

# Ej1-a Mostrar esquema de tipos y convertir columna "Fecha" 
# Mostrar nuevo esquema y 6 filas del DataFrame

def ejercicio_1a(df):
    print("Ej1-a")
    df.printSchema()


    df_new = df.withColumn("Fecha", regexp_replace(col("Fecha"), r"(\d{2})/(\d{2})/(\d{4})", r"$3-$2-$1"))
    df_new = df_new.withColumn("Fecha", col("Fecha").cast("date"))
    df_new.printSchema()
    df_new.show(6)

    return df_new

# Ej1-b Eliminar sufijo .MC de los nombres de las columnas

def ejercicio_1b(df):
    for i in df.columns:
        if ".MC" in i:
            df = df.withColumnRenamed(i, i[:-3])

    df.show(6)
    return df

# Ej1-c Definir StructType para cargar el tipo correcto de cada columna
# Sustituir nombre tickers por nombre/siglas empresa

def ejercicio_1c(df, spark_session):
    tickers = {
        "IBE": "Iberdrola",
        "REP": "Repsol",
        "NTGY": "Naturgy",
        "SAN": "Santander",
        "BBVA": "BBVA",
        "CABK": "CaixaBank",
        "BKT": "Bankinter",
        "SAB": "Sabadell",
        "UNI": "Unicaja",
        "TEF": "Telefonica",
        "ITX": "Inditex",
        "IDR": "Indra"
    }

    for i in df.columns:
        if i in tickers:
            df = df.withColumnRenamed(i, tickers[i])


    schema_fields = [StructField("Fecha", DateType(), True)]

    for i in df.columns:
        if i != "Fecha":
            schema_fields.append(StructField(i, DecimalType(10, 2), True))

    schema_ = StructType(schema_fields)

    df_schema = spark_session.read.option("header", True).option("sep", ";").option("dateFormat", "dd/MM/yyyy").schema(schema_).csv("ibex35_close_2024.csv")
    print("Ahora viene el schema")
    df_schema.printSchema()
    df_schema.show(6)

    return df
