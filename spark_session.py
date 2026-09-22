from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

spark_session = (SparkSession.builder.appName("IBEX35").getOrCreate())
df = spark_session.read.option("header", True).option("sep", ";").option("dateFormat", "dd/MM/yyyy").csv("ibex35_close_2024.csv")
print("========================================================================================================================")
print(df.columns)
print("========================================================================================================================")
primerosSeis = df.head(6)[0]
print(primerosSeis)