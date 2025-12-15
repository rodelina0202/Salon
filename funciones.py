from conexion import supabase, TABLA1, TABLA2, TABLA3, TABLA4
from utilidades import banner, imprimir_resultado, pausar, exportar_csv, exportar_json, exportar_sql
from datetime import datetime, timedelta

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# CRUD TABLA1 (Clientes)
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def agregar_cliente():
    try:
        banner("AGREGAR CLIENTE")
        first_name = input("Nombre: ").strip()
        last_name = input("Apellido: ").strip()
        phone = input("Teléfono: ").strip()
        email = input("Correo: ").strip()
        if not all([first_name, last_name, phone, email]):
            print("\nTodos los campos son obligatorios.")
            pausar()
            return
        supabase.table(TABLA1).insert({
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email
        }).execute()
        print("\nCliente agregado correctamente.")
    except Exception as e:
        print("Error:", e)
    pausar()

def listar_clientes():
    try:
        data = supabase.table(TABLA1).select("*").order("customer_id", desc=True).execute()
        banner("LISTA DE CLIENTES")
        for cliente in data.data or []:
            imprimir_resultado(cliente)
        opcion = input("¿Desea exportar la lista de clientes a csv / json / sql / no ? (csv/json/sql/no): ").strip().lower()
        if opcion == "csv":
            exportar_csv("clientes.csv", data.data or [])
        elif opcion == "json":
            exportar_json("clientes.json", data.data or [])
        elif opcion == "sql":
            exportar_sql("clientes.sql", data.data or [], TABLA1 or "clientes")
    except Exception as e:
        print("Error:", e)
    pausar()

def buscar_cliente():
    try:
        entrada = input("Cliente (ID o nombre): ").strip()
        if entrada.isdigit():
            cliente_id = int(entrada)
            data = supabase.table(TABLA1).select("*").eq("customer_id", cliente_id).execute()
        else:
            data = supabase.table(TABLA1).select("*").or_(
                f"first_name.ilike.%{entrada.lower()}%,last_name.ilike.%{entrada.lower()}%"
            ).execute()
        resultados = data.data if data.data else []
        banner("RESULTADOS")
        if not resultados:
            print("No se encontró ningún cliente.")
        else:
            for cliente in resultados:
                imprimir_resultado(cliente)
    except Exception as e:
        print("Error al buscar cliente:", e)
    pausar()

def eliminar_cliente():
    try:
        cliente_id = int(input("ID del cliente a eliminar: "))
        supabase.table(TABLA1).delete().eq("customer_id", cliente_id).execute()
        print("Cliente eliminado correctamente.")
    except Exception as e:
        print("Error:", e)
    pausar()

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# CRUD TABLA2 (Empleados)
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def agregar_empleado():
    try:
        banner("AGREGAR EMPLEADO")
        first_name = input("Nombre: ").strip()
        last_name = input("Apellido: ").strip()
        job_title = input("Cargo: ").strip()
        if not all([first_name, last_name, job_title]):
            print("\nTodos los campos son obligatorios.")
            pausar()
            return
        supabase.table(TABLA2).insert({
            "first_name": first_name,
            "last_name": last_name,
            "job_title": job_title
        }).execute()
        print("\nEmpleado agregado correctamente.")
    except Exception as e:
        print("Error:", e)
    pausar()

def listar_empleados():
    try:
        data = supabase.table(TABLA2).select("*").order("employee_id", desc=True).execute()
        banner("LISTA DE EMPLEADOS")
        for emp in data.data or []:
            imprimir_resultado(emp)
        opcion = input("¿Desea exportar la lista de empleados a csv / json / sql / no ? (csv/json/sql/no): ").strip().lower()
        if opcion == "csv":
            exportar_csv("empleados.csv", data.data or [])
        elif opcion == "json":
            exportar_json("empleados.json", data.data or [])
        elif opcion == "sql":
            exportar_sql("empleados.sql", data.data or [], TABLA2 or "empleados")
    except Exception as e:
        print("Error:", e)
    pausar()

def buscar_empleado():
    try:
        entrada = input("Empleado (ID o nombre): ").strip()
        if entrada.isdigit():
            emp_id = int(entrada)
            data = supabase.table(TABLA2).select("*").eq("employee_id", emp_id).execute()
        else:
            data = supabase.table(TABLA2).select("*").or_(
                f"first_name.ilike.%{entrada.lower()}%,last_name.ilike.%{entrada.lower()}%"
            ).execute()
        resultados = data.data if data.data else []
        banner("RESULTADOS")
        if not resultados:
            print("No existe un empleado con esa referencia.")
        else:
            for emp in resultados:
                imprimir_resultado(emp)
    except Exception as e:
        print("Error:", e)
    pausar()

def eliminar_empleado():
    try:
        emp_id = int(input("ID del empleado a eliminar: "))
        supabase.table(TABLA2).delete().eq("employee_id", emp_id).execute()
        print("Empleado eliminado correctamente.")
    except Exception as e:
        print("Error:", e)
    pausar()

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# CRUD TABLA3 (Servicios)
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def agregar_servicio():
    try:
        banner("AGREGAR SERVICIO")
        name = input("Nombre del servicio: ").strip()
        desc = input("Descripción: ").strip()
        price = input("Precio: ").strip()
        if not all([name, desc, price]):
            print("\nTodos los campos son obligatorios.")
            pausar()
            return
        price = float(price)
        supabase.table(TABLA3).insert({
            "service_name": name,
            "description": desc,
            "price": price
        }).execute()
        print("\nServicio agregado correctamente.")
    except Exception as e:
        print("Error:", e)
    pausar()

def listar_servicios():
    try:
        data = supabase.table(TABLA3).select("*").order("service_id", desc=True).execute()
        banner("LISTA DE SERVICIOS")
        for s in data.data or []:
            imprimir_resultado(s)
        opcion = input("¿Desea exportar la lista de servicios a csv / json / sql / no ? (csv/json/sql/no): ").strip().lower()
        if opcion == "csv":
            exportar_csv("servicios.csv", data.data or [])
        elif opcion == "json":
            exportar_json("servicios.json", data.data or [])
        elif opcion == "sql":
            exportar_sql("servicios.sql", data.data or [], TABLA3 or "servicios")
    except Exception as e:
        print("Error:", e)
    pausar()

def buscar_servicio():
    try:
        entrada = input("Servicio (ID o nombre): ").strip()
        if entrada.isdigit():
            serv_id = int(entrada)
            data = supabase.table(TABLA3).select("*").eq("service_id", serv_id).execute()
        else:
            data = supabase.table(TABLA3).select("*").ilike("service_name", f"%{entrada.lower()}%").execute()
        resultados = data.data if data.data else []
        banner("RESULTADOS")
        if not resultados:
            print("No existe ese servicio.")
        else:
            for s in resultados:
                imprimir_resultado(s)
    except Exception as e:
        print("Error:", e)
    pausar()

def eliminar_servicio():
    try:
        serv_id = int(input("ID del servicio a eliminar: "))
        supabase.table(TABLA3).delete().eq("service_id", serv_id).execute()
        print("Servicio eliminado correctamente.")
    except Exception as e:
        print("Error:", e)
    pausar()

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# CRUD TABLA4 (Citas)
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def agregar_cita():
    try:
        banner("AGREGAR CITA")
        customer_id = input("ID Cliente: ").strip()
        employee_id = input("ID Empleado: ").strip()
        service_id = input("ID Servicio: ").strip()
        date = input("Fecha (YYYY-MM-DD): ").strip()
        notes = input("Notas: ").strip()
        if not customer_id or not employee_id or not service_id or not date:
            print("\nLos campos ID y fecha son obligatorios.")
            pausar()
            return
        customer_id = int(customer_id)
        employee_id = int(employee_id)
        service_id = int(service_id)
        supabase.table(TABLA4).insert({
            "customer_id": customer_id,
            "employee_id": employee_id,
            "service_id": service_id,
            "appointment_date": date,
            "notes": notes
        }).execute()
        print("\nCita creada correctamente.")
    except Exception as e:
        print("Error:", e)
    pausar()

def listar_citas():
    try:
        data = supabase.table(TABLA4).select("*").order("appointment_id", desc=True).execute()
        banner("LISTA DE CITAS")
        for c in data.data or []:
            imprimir_resultado(c)
        opcion = input("¿Desea exportar la lista de citas a csv / json / sql / no ? (csv/json/sql/no): ").strip().lower()
        if opcion == "csv":
            exportar_csv("citas.csv", data.data or [])
        elif opcion == "json":
            exportar_json("citas.json", data.data or [])
        elif opcion == "sql":
            exportar_sql("citas.sql", data.data or [], TABLA4 or "citas")
    except Exception as e:
        print("Error:", e)
    pausar()

def buscar_cita():
    try:
        cita_id = int(input("ID de la cita: "))
        data = supabase.table(TABLA4).select("*").eq("appointment_id", cita_id).execute()
        banner("RESULTADO")
        if data.data:
            imprimir_resultado(data.data[0])
        else:
            print("No existe una cita con ese ID.")
    except Exception as e:
        print("Error:", e)
    pausar()

def eliminar_cita():
    try:
        cita_id = int(input("ID de la cita a eliminar: "))
        supabase.table(TABLA4).delete().eq("appointment_id", cita_id).execute()
        print("Cita eliminada correctamente.")
    except Exception as e:
        print("Error:", e)
    pausar()

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# MÓDULO ADMINISTRATIVO 
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def citas_por_dia():
    try:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
        data = supabase.table(TABLA4).select("*").eq("appointment_date", fecha).execute()
        banner(f"CITAS DEL DÍA {fecha}")
        if data.data:
            for c in data.data:
                imprimir_resultado(c)
        else:
            print("No hay citas en esa fecha.")
    except Exception as e:
        print("Error:", e)
    pausar()

def total_ganancias():
    try:
        data_citas = supabase.table(TABLA4).select("*").execute()
        total = 0.0
        if data_citas.data:
            for cita in data_citas.data:
                servicio = supabase.table(TABLA3).select("price").eq("service_id", cita.get("service_id")).execute()
                if servicio.data and servicio.data[0].get("price") is not None:
                    try:
                        total += float(servicio.data[0]["price"])
                    except Exception:
                        pass
        banner("TOTAL DE GANANCIAS")
        print(f"Ganancia total: ${total:.2f}")
    except Exception as e:
        print("Error:", e)
    pausar()

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# NUEVAS FUNCIONES ADMINISTRATIVAS
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def citas_por_dia():
   
    try:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
        # Obtener todas las citas del día
        data_citas = supabase.table(TABLA4).select("*").eq("appointment_date", fecha).execute()
        banner(f"CITAS Y GANANCIAS DEL DÍA {fecha}")
        total = 0.0
        if data_citas.data:
            for cita in data_citas.data:
                # Mostrar cada cita
                imprimir_resultado(cita)
                # Obtener el precio del servicio de esa cita
                servicio = supabase.table(TABLA3).select("price").eq("service_id", cita.get("service_id")).execute()
                if servicio.data and servicio.data[0].get("price") is not None:
                    try:
                        total += float(servicio.data[0]["price"])
                    except Exception:
                        pass
            print(f"\nGanancia total del día: ${total:.2f}")
        else:
            print("No hay citas registradas en esa fecha.")
    except Exception as e:
        print("Error al obtener citas por día:", e)
    pausar()

def ganancias_por_mes():
    try:
        mes = input("Ingrese mes y año (MM-YYYY): ").strip()
        month, year = map(int, mes.split("-"))
        data_citas = supabase.table(TABLA4).select("*").execute()
        total = 0.0
        if data_citas.data:
            for cita in data_citas.data:
                fecha_cita = datetime.strptime(cita.get("appointment_date"), "%Y-%m-%d")
                if fecha_cita.month == month and fecha_cita.year == year:
                    servicio = supabase.table(TABLA3).select("price").eq("service_id", cita.get("service_id")).execute()
                    if servicio.data and servicio.data[0].get("price") is not None:
                        try:
                            total += float(servicio.data[0]["price"])
                        except Exception:
                            pass
        banner(f"GANANCIAS DEL MES {mes}")
        print(f"Ganancia total: ${total:.2f}")
    except Exception as e:
        print("Error:", e)
    pausar()

def resumen_semanal():
    try:
        hoy = datetime.today()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        fin_semana = inicio_semana + timedelta(days=6)
        data_citas = supabase.table(TABLA4).select("*").execute()
        total = 0.0
        completadas = 0
        pendientes = 0
        citas_lista = []
        if data_citas.data:
            for cita in data_citas.data:
                fecha_cita = datetime.strptime(cita.get("appointment_date"), "%Y-%m-%d")
                if inicio_semana <= fecha_cita <= fin_semana:
                    citas_lista.append(cita)
                    servicio = supabase.table(TABLA3).select("price").eq("service_id", cita.get("service_id")).execute()
                    if servicio.data and servicio.data[0].get("price") is not None:
                        try:
                            total += float(servicio.data[0]["price"])
                        except Exception:
                            pass
                    if cita.get("notes"):
                        completadas += 1
                    else:
                        pendientes += 1
        banner(f"RESUMEN SEMANAL ({inicio_semana.date()} a {fin_semana.date()})")
        print(f"Total ganancias: ${total:.2f}")
        print(f"Citas completadas: {completadas}")
        print(f"Citas pendientes: {pendientes}")
        print("\nDetalle de citas:")
        for c in citas_lista:
            imprimir_resultado(c)
    except Exception as e:
        print("Error:", e)
    pausar()