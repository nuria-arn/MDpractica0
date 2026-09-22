from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

spark_session = (SparkSession.builder.appName("IBEX35").getOrCreate())
df = spark_session.read.option("header", True).option("sep", ";").option("dateFormat", "dd/MM/yyyy").csv("ibex35_close_2024.csv")

# Ej1-a Mostrar esquema de tipos y convertir columna "Fecha" 
# Mostrar nuevo esquema y 6 filas del DataFrame

print("Ej1-a")
df.printSchema()

# print("========================================================================================================================")

df_new = df.withColumn("Fecha", to_date(col("Fecha"), "dd/MM/yyyy"))
df_new = df_new.withColumn("Fecha", col("Fecha").cast("date"))
df_new.printSchema()
print(df_new.show(6))