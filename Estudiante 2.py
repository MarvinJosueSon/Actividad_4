class Medicamento:

    def Mostrar(self):
        print(f"Nombre: {self.nombre}; Precio: {self.precio}")
MedicamentosPila=[]

while True:
    try:
        print("==Medicamentos==")
        print("1. Ingresesar Medicamento")
        print("2. Entregar Medicamento")
        print("3. Medicamentos pendientes")
        print("4. Salir")
        opcion=input("Ingrese la opcion: ")
        match opcion:
            case "1":
                try:
                    nombreAux=input("Ingrese el nombre del medicamento: ")
                    precioAux=int(input("Ingrese el precio del medicamento: "))
                    medicamentoAux=Medicamento(nombreAux,precioAux)
                    MedicamentosPila.append(medicamentoAux)
                except ValueError:
                    print("ERROR EN LOS DATOS")
            case "2":
                if len(MedicamentosPila) > 0:
                    print("Entregando el medicamento:")
                    MedicamentosPila.pop().Mostrar()
                else:
                    print("No hay medicamentos por entregar.")
            case "3":
                print("Medicamentos en cola: ")
                for medicamento in MedicamentosPila:
                    medicamento.Mostrar()
            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opcion no encontrada")
    except ValueError:
        print("ERROR EN LOS DATOS")
