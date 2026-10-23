from excepciones import StringException, EnteroPositivoException


class Empleado:
    def __init__(self, nombre: str, sueldo: int):
        self.legajo = None
        self.set_nombre(nombre)
        self.set_sueldo(sueldo)

    def set_nombre(self, nombre: str):
        if not isinstance(nombre, str) or len(nombre) < 3:
            raise StringException(
                "El nombre del empleado debe tener 3 o mas caracteres."
            )
        self.nombre = nombre

    def set_sueldo(self, sueldo: int):
        if type(sueldo) is not int or sueldo <= 0:
            raise EnteroPositivoException(
                "El sueldo del empleado debe ser mayor a 0."
            )
        self.sueldo = sueldo

    def set_legajo(self, legajo: int):
        if type(legajo) is not int or legajo <= 0:
            raise EnteroPositivoException(
                "El legajo del empleado debe ser mayor a 0."
            )
        self.legajo = legajo
