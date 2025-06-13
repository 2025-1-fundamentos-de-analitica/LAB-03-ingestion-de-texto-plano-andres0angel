import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = lines[4:]

    registros = []
    registro_actual = []

    for line in lines:
        if re.match(r"^\s*\d+\s{2,}", line):
            if registro_actual:
                registros.append(registro_actual)
            registro_actual = [line.strip()]
        else:
            registro_actual.append(line.strip())

    if registro_actual:
        registros.append(registro_actual)

    data = []
    for reg in registros:
        completo = " ".join(reg)
        completo = re.sub(r"\s{2,}", "|", completo)
        partes = completo.split("|")

        cluster = int(partes[0])
        cantidad = int(partes[1])
        porcentaje = float(partes[2].replace(",", ".").replace("%", "").strip())
        palabras = " ".join(partes[3:])

        palabras = re.sub(r"\s+", " ", palabras)
        palabras = palabras.replace(".,", ".").replace(".,", ".")
        palabras = palabras.replace(", ", ",").replace(",", ", ")
        palabras = palabras.strip(", ")

        palabras = palabras.rstrip('.')  # <-- AQUI ESTA LA CORRECCION

        data.append((cluster, cantidad, porcentaje, palabras))

    df = pd.DataFrame(data, columns=["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"])
    return df
