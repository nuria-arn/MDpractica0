from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

# Ej3: Modifica

def ejercicio3(df):
    print("Ej3")

    df = df.withColumnRenamed("Fecha", "Dia")
    df.show(10)

    print("\nMedias de las empresas:")
    medias = {}
    for c in df.columns:
        if c != "Dia":
            medias[c] =df.agg( round( avg(c), 3)).head(1)[0][0]

    for c, media in medias.items():
        print(f"{c}: {media}")


    print("\nMáximos de las empresas:")
    maximos = {}
    for c in df.columns:
        if c != "Dia":
            maximos[c] =df.agg(max(c)).head(1)[0][0]

    for c, maximo in maximos.items():
        print(f"{c}: {maximo}")


    print("\nMínimos de las empresas:")
    minimos = {}
    for c in df.columns:
        if c != "Dia":
            minimos[c] =df.agg(min(c)).head(1)[0][0]

    for c, minimo in minimos.items():
        print(f"{c}: {minimo}")


    df = df.withColumn("Deficiency Notice UNI", when(col("Unicaja")<=1.00, True).otherwise(False))
    df.show(100)

    return(df)