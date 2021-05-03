"""Herencia"""


# NO MODIFICAR - INICIO
from dataclasses import dataclass


class Animal:
    def __init__(self, edad: int = 0):
        self.edad = edad

    def descripcion(self) -> str:
        return f"Tengo {self.edad} años"
# NO MODIFICAR - FIN


class Perro(Animal):
    """Escribir un constructor que añada una variable de instancia llamada raza,
    de tipo string y que tenga como valor por defecto "". Adicionalmente se debe
    sobrecargar el método descripción para que devuelva:
    "Soy un perro y" + método descripción del padre
    """

    def __init__(self, raza: str = "", edad: int = 0) -> None:
        super().__init__(edad)
        self.raza: str = raza

    def descripcion(self) -> str:
        return f'Soy un perro y {super().descripcion().lower()}'


# NO MODIFICAR - INICIO
terrier = Perro(edad=8, raza="Yorkshire Terrier")
cachorro = Perro(edad=1)
dogo = Perro(raza="Dogo")

assert Animal(10).descripcion() == "Tengo 10 años"
assert terrier.descripcion() == "Soy un perro y tengo 8 años"
assert dogo.descripcion() == "Soy un perro y tengo 0 años"
assert cachorro.descripcion() == "Soy un perro y tengo 1 años"
# NO MODIFICAR - FIN

"""Re-Escribir utilizando DataClasses"""


@dataclass
class Animal:
    edad: int = 0

    def descripcion(self) -> str:
        return f"Tengo {self.edad} años"


@dataclass
class Perro(Animal):
    raza: str = ""

    def descripcion(self) -> str:
        return f"Soy un perro y {super().descripcion().lower()}"


# NO MODIFICAR - INICIO
terrier = Perro(edad=8, raza="Yorkshire Terrier")
cachorro = Perro(edad=1)
dogo = Perro(raza="Dogo")

assert Animal(10).descripcion() == "Tengo 10 años"
assert terrier.descripcion() == "Soy un perro y tengo 8 años"
assert dogo.descripcion() == "Soy un perro y tengo 0 años"
assert cachorro.descripcion() == "Soy un perro y tengo 1 años"
# NO MODIFICAR - FIN
