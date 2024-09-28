#Juego desarrollo sotenible

import random
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def describir(self):
        pass

class Trabajador(Persona):
    def __init__(self, nombre, salario, horas_trabajo, experiencia):
        super().__init__(nombre)
        self.salario = salario
        self.horas_trabajo = horas_trabajo
        self.experiencia = experiencia

    def describir(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario}, Horas de trabajo: {self.horas_trabajo}, Experiencia: {self.experiencia}"

    def trabajar(self):
        return f"{self.nombre} está trabajando."

class Manager(Trabajador):
    def __init__(self, nombre, salario, horas_trabajo, experiencia, equipo):
        super().__init__(nombre, salario, horas_trabajo, experiencia)
        self.equipo = equipo

    def describir(self):
        descripcion = super().describir()
        descripcion += f", Equipo: {', '.join([miembro.nombre for miembro in self.equipo])}"
        return descripcion

    def gestionar(self):
        return f"{self.nombre} está gestionando al equipo."

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = []
        self.crecimiento = 0

    def contratar(self, trabajador):
        self.trabajadores.append(trabajador)

    def despedir(self, trabajador):
        self.trabajadores.remove(trabajador)

    def crecimiento_economico(self, puntos):
        self.crecimiento += puntos

    def verificar_empleo(self):
        novato_presente = any(isinstance(trabajador, Trabajador) and trabajador.experiencia == "novato" for trabajador in self.trabajadores)
        return novato_presente

    def condiciones_aptas(self, trabajador):
        if trabajador.salario * trabajador.horas_trabajo * 30 < 1000:  # Verifica si el salario mensual es inferior a $1000
            return False
        return True

    def mostrar_trabajadores(self):
        for trabajador in self.trabajadores:
            print(trabajador.describir())