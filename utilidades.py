import os
import csv
import json
from datetime import datetime

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# UTILIDADES DE TERMINAL
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresiona ENTER para continuar...")

def banner(titulo):
    print("╔" + "═" * 42 + "╗")
    print("║" + titulo.center(42) + "║")
    print("╚" + "═" * 42 + "╝")

def imprimir_resultado(fila):
    print("\n" + "═" * 40)
    for clave, valor in fila.items():
        print(f"{clave.capitalize():<15}: {valor}")
    print("═" * 40 + "\n")

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXPORTACIÓN DE DATOS
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def exportar_csv(nombre_archivo, datos):
    if not datos:
        print("No hay datos para exportar.")
        return
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(datos[0].keys()))
        escritor.writeheader()
        escritor.writerows(datos)
    print(f"Datos exportados correctamente a {nombre_archivo}")

def exportar_json(nombre_archivo, datos):
    if not datos:
        print("No hay datos para exportar.")
        return
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
    print(f"Datos exportados correctamente a {nombre_archivo}")

def _adivinar_tipo_columna(nombre_columna, valor_ejemplo):
    n = nombre_columna.lower()
    if n.endswith("_id") or n in ("id", "customer_id", "employee_id", "service_id", "appointment_id"):
        return "INTEGER"
    if "price" in n or "precio" in n or isinstance(valor_ejemplo, (int, float)):
        return "NUMERIC"
    if "date" in n or "fecha" in n:
        return "DATE"
    return "TEXT"

def _formatear_valor_sql(valor):
    if valor is None:
        return "NULL"
    if isinstance(valor, (int, float)):
        return str(valor)
    try:
        if isinstance(valor, str):
            v = valor.strip()
            if v == "":
                return "NULL"
            if v.replace('.', '', 1).isdigit() and v.count('.') <= 1:
                return v
    except Exception:
        pass
    s = str(valor).replace("'", "''")
    return f"'{s}'"

def exportar_sql(nombre_archivo, datos, nombre_tabla):
    if not datos:
        print("No hay datos para exportar.")
        return

    columnas = list(datos[0].keys())
    tipos = {}
    for col in columnas:
        ejemplo = None
        for fila in datos:
            if fila.get(col) is not None:
                ejemplo = fila.get(col)
                break
        tipos[col] = _adivinar_tipo_columna(col, ejemplo)

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"-- Exportado desde Rode's Salón - {datetime.now().isoformat()}\n")
        f.write(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} (\n")
        defs = []
        for col in columnas:
            defs.append(f"  {col} {tipos[col]}")
        f.write(",\n".join(defs))
        f.write("\n);\n\n")

        for fila in datos:
            valores = [_formatear_valor_sql(fila.get(c)) for c in columnas]
            f.write(f"INSERT INTO {nombre_tabla} ({', '.join(columnas)}) VALUES ({', '.join(valores)});\n")

    print(f"Datos exportados correctamente a {nombre_archivo}")
