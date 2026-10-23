from empleado import Empleado
from excepciones import CollectionVaciaException, NoEncontradoException


class EmpleadoService:
    empleados = []
    proximo_legajo = 1

    @classmethod
    def agregar(cls, empleado: Empleado) -> bool:
        empleado.set_legajo(cls.proximo_legajo)
        cls.proximo_legajo += 1
        cls.empleados.append(empleado)
        return True

    @classmethod
    def mayor_sueldo(cls) -> Empleado:
        if not cls.empleados:
            raise CollectionVaciaException("No hay empleados.")
        return max(cls.empleados, key=lambda e: e.sueldo)

    @classmethod
    def sueldo_promedio(cls) -> float:
        if not cls.empleados:
            raise CollectionVaciaException("No hay empleados.")
        total = sum(e.sueldo for e in cls.empleados)
        return total / len(cls.empleados)

    @classmethod
    def eliminar(cls, nombre: str):
        if not cls.empleados:
            raise CollectionVaciaException("No hay empleados.")
        if not any(e.nombre == nombre for e in cls.empleados):
            raise NoEncontradoException("No se encontro el empleado.")
        cls.empleados = [e for e in cls.empleados if e.nombre != nombre]
