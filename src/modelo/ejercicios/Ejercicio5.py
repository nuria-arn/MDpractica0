from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *


# Ej5: Seguimiento del año que viene

def ejercicio5(df):
    print("Ej5: ")

    for c in df.columns:
        if c != "Dia" and c != "Deficiency Notice UNI":
            df = df.withColumn(c, col(c).cast("double"))

    cuartiles = {}
    for c in df.columns:
        if c != "Dia" and c != "Deficiency Notice UNI":
            q1, q2, q3 = df.approxQuantile(c, [0.25, 0.50, 0.75], 0.0)
            cuartiles[c] = (q1, q2, q3)

    for c in df.columns:
        if c != "Dia" and c != "Deficiency Notice UNI":
            q1, q2, q3 = cuartiles[c]
            df = df.withColumn(c+"Cuartil", when(col(c).isNull(), None).when(col(c) <= q1, "q1").when(col(c) <= q2, "q2").when(col(c) <= q3, "q3").otherwise("q4"))

    df.show(1)

    df.select(
        "Dia",
        "AENA",
        "AENACuartil",
        "BBVA",
        "BBVACuartil"
    ).show()

    return df