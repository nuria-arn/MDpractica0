from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

# Ej4: Variacion Anual

def ejercicio4(df):
    print("Ej4: ")

    variacion_an = {}
    for c in df.columns:
        if c != "Dia" and c != "Deficiency Notice UNI":
            no_nulo = df.select("Dia", c).where(col(c).isNotNull())

            fecha_minima = no_nulo.orderBy(col("Dia").asc()).head(1)[0]
            fecha_maxima = no_nulo.orderBy(col("Dia").desc()).head(1)[0]


            inicial = fecha_minima[c]
            final = fecha_maxima[c]        

            variacion = ((float(final) - float(inicial)) / float(inicial)) * 100

            if variacion <= -15:
                variacion_an[c] = "Bajada Fuerte"
            elif variacion < -1:
                variacion_an[c] = "Bajada"
            elif variacion <= 1:
                variacion_an[c] = "Neutra"
            elif variacion < 15:
                variacion_an[c] = "Subida"
            else:
                variacion_an[c] = "Subida Fuerte"

    for c, variacion in variacion_an.items():
        print(f"{c}: {variacion}")