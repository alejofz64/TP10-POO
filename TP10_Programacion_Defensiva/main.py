from empleado import Empleado
from empleado_service import EmpleadoService
from excepciones import (
    StringException,
    EnteroPositivoException,
    CollectionVaciaException,
    NoEncontradoException,
)


if __name__ == "__main__":
    print("1. Intento crear un empleado con un nombre invalido")
    try:
        Empleado("Al", 100000)
    except StringException as e:
        print("Error:", e)

    print("\n2. Intento crear un empleado con un sueldo negativo")
    try:
        Empleado("Juan", -5000)
    except EnteroPositivoException as e:
        print("Error:", e)

    print("\n3. Intento calcular el promedio con la lista vacia")
    try:
        EmpleadoService.sueldo_promedio()
    except CollectionVaciaException as e:
        print("Error:", e)

    print("\n4. Agrego dos empleados validos")
    ana = Empleado("Ana", 100000)
    juan = Empleado("Juan", 200000)
    EmpleadoService.agregar(ana)
    EmpleadoService.agregar(juan)
    print(f"{ana.nombre}: legajo {ana.legajo}, sueldo {ana.sueldo}")
    print(f"{juan.nombre}: legajo {juan.legajo}, sueldo {juan.sueldo}")

    print("\n5. Intento eliminar un empleado que no existe")
    try:
        EmpleadoService.eliminar("Pedro")
    except NoEncontradoException as e:
        print("Error:", e)

    print("\n6. Compruebo las operaciones normales")
    mejor_pago = EmpleadoService.mayor_sueldo()
    print("Mayor sueldo:", mejor_pago.nombre, mejor_pago.sueldo)
    print("Sueldo promedio:", EmpleadoService.sueldo_promedio())

    print("\n7. Intento modificar un sueldo con valor 0")
    try:
        ana.set_sueldo(0)
    except EnteroPositivoException as e:
        print("Error:", e)
    print("El sueldo de Ana sigue siendo:", ana.sueldo)

