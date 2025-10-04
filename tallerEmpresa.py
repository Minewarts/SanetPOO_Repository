import random

def GenerarId(prefijo, ids_existentes):
    while True:
        num = random.randint(10000, 99999)
        nuevo_id = f"#{prefijo}{num}"
        if nuevo_id not in ids_existentes:
            ids_existentes.add(nuevo_id)
            return nuevo_id

class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def Presentarse(self):
        print(f"Hola, soy {self.nombre}")

class Empleado(Persona):
    ids_empleados = set()

    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo)
        self.id = GenerarId("EMP", Empleado.ids_empleados)
        self.salario = salario

    def CalcularBono(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguaje_principal):
        super().__init__(nombre, correo, salario)
        self.lenguaje_principal = lenguaje_principal
        self.tareas_asignadas = []

    def CalcularBono(self):
        bono_base = 0.10 * self.salario
        bono_extra = 0.01 * self.salario if len(self.tareas_asignadas) > 5 else 0
        return bono_base + bono_extra

class Analista(Empleado):
    def __init__(self, nombre, correo, salario, seniority):
        super().__init__(nombre, correo, salario)
        self.seniority = seniority.lower()

    def CalcularBono(self):
        bono = 0.08 * self.salario
        if self.seniority == "senior":
            bono += 0.03 * self.salario
        return bono

class Gerente(Empleado):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo, salario)
        self.equipo = []

    def AgregarEmpleado(self, empleado):
        if empleado is self:
            print("No puedes agregarte a ti mismo como subordinado.")
            return
        if empleado in self.equipo:
            print("Este empleado ya está en el equipo.")
            return
        self.equipo.append(empleado)
        print(f"{empleado.nombre} fue agregado al equipo de {self.nombre}.")

    def RemoverEmpleado(self, empleado):
        if empleado in self.equipo:
            self.equipo.remove(empleado)
            print(f"{empleado.nombre} fue removido del equipo de {self.nombre}.")
        else:
            print("El empleado no está en el equipo.")

    def ListarEquipo(self):
        print(f"Equipo de {self.nombre}:")
        if not self.equipo:
            print("   (sin empleados a cargo)")
        for e in self.equipo:
            print(f"- {e}")

    def CalcularBono(self):
        return len(self.equipo) * 0.02 * self.salario

class Tarea:
    ids_tareas = set()

    def __init__(self, descripcion, horas_estimadas):
        if horas_estimadas < 0:
            raise ValueError("Las horas estimadas no pueden ser negativas.")
        self.id = GenerarId("TAR", Tarea.ids_tareas)
        self.descripcion = descripcion
        self.horas_estimadas = horas_estimadas
        self.asignado_a = None

    def AsignarEmpleado(self, empleado):
        self.asignado_a = empleado
        if isinstance(empleado, Desarrollador):
            empleado.tareas_asignadas.append(self)

class Proyecto:
    ids_proyectos = set()

    def __init__(self, nombre, presupuesto):
        self.id = GenerarId("PRY", Proyecto.ids_proyectos)
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.tareas = []
        self.empleados_asignados = []

    def AgregarEmpleado(self, empleado):
        if empleado in self.empleados_asignados:
            print(f"El empleado {empleado.nombre} ya está asignado a este proyecto.")
            return
        self.empleados_asignados.append(empleado)
        print(f"Empleado {empleado.nombre} asignado al proyecto '{self.nombre}'.")

    def AgregarTarea(self, descripcion, horas_estimadas):
        try:
            nueva_tarea = Tarea(descripcion, horas_estimadas)
            self.tareas.append(nueva_tarea)
            print(f"Tarea '{descripcion}' agregada al proyecto '{self.nombre}' ({nueva_tarea.id})")
        except ValueError as e:
            print(e)

    def AsignarEmpleado(self, tarea_id, empleado):
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.AsignarEmpleado(empleado)
                print(f"Empleado {empleado.nombre} asignado a tarea '{tarea.descripcion}'.")
                return
        print("Tarea no encontrada.")

    def ListarTareas(self):
        print(f"Tareas del proyecto '{self.nombre}' ({self.id}):")
        if not self.tareas:
            print("   (sin tareas registradas)")
        for tarea in self.tareas:
            asignado = tarea.asignado_a.nombre if tarea.asignado_a else "Nadie"
            print(f"- [{tarea.id}] {tarea.descripcion} ({tarea.horas_estimadas}h) → {asignado}")

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.proyectos = []

    def AgregarEmpleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado '{empleado.nombre}' agregado con ID {empleado.id}.")

    def CrearProyecto(self, nombre, presupuesto):
        nuevo_proyecto = Proyecto(nombre, presupuesto)
        self.proyectos.append(nuevo_proyecto)
        print(f"Proyecto '{nombre}' creado con ID {nuevo_proyecto.id}.")
        return nuevo_proyecto

    def AsignarEmpleadoAProyecto(self, proyecto, empleado):
        proyecto.AgregarEmpleado(empleado)

# --- Programa principal ---
empresa = Empresa("SaNTECH")
print("=======|=== ¡Bienvenido SaNTECH! ===|=======")
while True:
    print("\n--------||---Menu---||--------")
    print("1. Agregar empleado")
    print("2. Crear proyecto")
    print("3. Agregar tarea a proyecto")
    print("4. Asignar empleado a proyecto")
    print("5. Asignar empleado a tarea")
    print("6. Listar tareas de un proyecto")
    print("7. Mostrar información de un empleado")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        salario = float(input("Salario: "))
        tipo = input("Tipo (desarrollador/analista/gerente): ").lower()

        if tipo == "desarrollador":
            lenguaje = input("Lenguaje principal: ")
            e = Desarrollador(nombre, correo, salario, lenguaje)
        elif tipo == "analista":
            seniority = input("Seniority (junior/senior): ")
            e = Analista(nombre, correo, salario, seniority)
        elif tipo == "gerente":
            e = Gerente(nombre, correo, salario)
        else:
            print("Tipo inválido.")
            continue
        empresa.AgregarEmpleado(e)

    elif opcion == "2":
        nombre = input("Nombre del proyecto: ")
        presupuesto = float(input("Presupuesto: "))
        empresa.CrearProyecto(nombre, presupuesto)

    elif opcion == "3":
        if not empresa.proyectos:
            print("No hay proyectos creados.")
            continue
        for i, p in enumerate(empresa.proyectos):
            print(f"{i+1}. {p.nombre} ({p.id})")
        idx = int(input("Seleccione proyecto: ")) - 1
        descripcion = input("Descripción de la tarea: ")
        horas = float(input("Horas estimadas: "))
        empresa.proyectos[idx].AgregarTarea(descripcion, horas)

    elif opcion == "4":
        if not empresa.proyectos or not empresa.empleados:
            print("Debe haber al menos un proyecto y un empleado.")
            continue

        for i, p in enumerate(empresa.proyectos):
            print(f"{i+1}. {p.nombre} ({p.id})")
        idx = int(input("Seleccione proyecto: ")) - 1
        proyecto = empresa.proyectos[idx]

        for i, e in enumerate(empresa.empleados):
            print(f"{i+1}. {e.nombre} ({e.id})")
        emp_idx = int(input("Seleccione empleado: ")) - 1
        empleado = empresa.empleados[emp_idx]

        empresa.AsignarEmpleadoAProyecto(proyecto, empleado)

    elif opcion == "5":
        if not empresa.proyectos or not empresa.empleados:
            print("Debe haber al menos un proyecto y un empleado.")
            continue

        for i, p in enumerate(empresa.proyectos):
            print(f"{i+1}. {p.nombre} ({p.id})")
        idx = int(input("Seleccione proyecto: ")) - 1
        proyecto = empresa.proyectos[idx]

        proyecto.ListarTareas()
        tarea_id = input("Ingrese el ID de la tarea (ej: #TAR12345): ")

        tarea = next((t for t in proyecto.tareas if t.id == tarea_id), None)
        if not tarea:
            print("Esa tarea no pertenece al proyecto seleccionado.")
            continuar = input("¿Desea buscar esa tarea en otro proyecto? (s/n): ").lower()
            if continuar == "s":
                for pr in empresa.proyectos:
                    tarea = next((t for t in pr.tareas if t.id == tarea_id), None)
                    if tarea:
                        print(f"Tarea encontrada en el proyecto '{pr.nombre}'.")
                        proyecto = pr
                        break
            if not tarea:
                print("Tarea no encontrada en ningún proyecto.")
                continue

        for i, e in enumerate(empresa.empleados):
            print(f"{i+1}. {e.nombre} ({e.id})")
        emp_idx = int(input("Seleccione empleado: ")) - 1
        empleado = empresa.empleados[emp_idx]

        proyecto.AsignarEmpleado(tarea.id, empleado)

    elif opcion == "6":
        for i, p in enumerate(empresa.proyectos):
            print(f"{i+1}. {p.nombre} ({p.id})")
        idx = int(input("Seleccione proyecto: ")) - 1
        empresa.proyectos[idx].ListarTareas()

    elif opcion == "7":
        if not empresa.empleados:
            print("No hay empleados registrados.")
            continue

        for i, e in enumerate(empresa.empleados):
            print(f"{i+1}. {e.nombre} ({e.id})")
        idx = int(input("Seleccione empleado: ")) - 1
        empleado = empresa.empleados[idx]

        bono = empleado.CalcularBono()
        salario_total = empleado.salario + bono

        print("\n--- Información del empleado ---")
        print(f"Nombre: {empleado.nombre}")
        print(f"ID: {empleado.id}")
        print(f"Salario base: ${empleado.salario:,.2f}")
        print(f"Bono: ${bono:,.2f}")
        print(f"Salario total (con bono): ${salario_total:,.2f}")

    elif opcion == "8":
        print("Saliendo del sistema.")
        break

    else:
        print("Opción no válida.")