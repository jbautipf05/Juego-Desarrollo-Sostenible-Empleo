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
            
print("¡Bienvenido a Owner, un juego donde serás dueño de una empresa que vela por el trabajo decente y el crecimiento económico! (ODS 8)")
print("En este juego, tendrás la oportunidad de tomar decisiones que afectarán el desarrollo económico de una empresa y el bienestar de sus trabajadores.")
print("Tu objetivo será lograr un equilibrio entre el trabajo decente y el crecimiento económico para alcanzar un desarrollo sostenible.\n")

nombre_empresa = input("Tienes que crear una empresa ya que no te encuentras en una buena situacion económica, crees que un buen nombre es...: ")
mi_empresa = Empresa(nombre_empresa)

# Contratación del primer trabajador
nombre_trabajador = input("Has estado trabajando, y parece que te llega un aspirante a trabajar en la empresa pues confia en esta, su nombre es: ")
salario_trabajador = float(input(f"Ingrese el salario por hora de {nombre_trabajador}: $"))
horas_trabajo = int(input(f"Ingrese las horas de trabajo por día de {nombre_trabajador}: "))
experiencia_trabajador = input(f"Ingrese la experiencia de {nombre_trabajador} (novato, medio, experimentado): ")

primer_trabajador = Trabajador(nombre_trabajador, salario_trabajador * horas_trabajo, horas_trabajo, experiencia_trabajador)

if salario_trabajador * horas_trabajo * 30 < 1000:
    print(f"Lo siento, {nombre_trabajador}, el salario ofrecido es demasiado bajo y no ha aceptado el trato, tienes que continuar solo")
else:
    if mi_empresa.condiciones_aptas(primer_trabajador):
        mi_empresa.contratar(primer_trabajador)
        print(f"Has contratado a {nombre_trabajador} con un salario de ${primer_trabajador.salario} por día y trabajará {primer_trabajador.horas_trabajo} horas por día.")
    else:
        print("No has cumplido con las condiciones laborales mínimas para los trabajadores. El juego no puede continuar.")
        exit()