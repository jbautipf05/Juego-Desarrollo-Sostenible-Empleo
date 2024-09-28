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

# Primera tanda de preguntas
respuestas_correctas = 0
situaciones = [
    ("El mercado está en auge y tienes la oportunidad de expandir tu negocio. ¿Expandir (E) o Consolidar (C)?", 'E',
     "Decidiste no aprovechar el mercado en auge para expandir tu negocio. Como resultado, tu competencia ganó más cuota de mercado."),
    ("Un cliente importante tiene una queja sobre la calidad del servicio. ¿Ofrecer un reembolso (R) o Ignorar la queja (I)?", 'R',
     "Decidiste ignorar la queja de un cliente importante. Esto resultó en una mala reputación para tu empresa y la pérdida de futuros clientes."),
    ("Un empleado sugiere una nueva idea para mejorar la eficiencia. ¿Implementar (I) o Rechazar (R)?", 'I',
     "Decidiste rechazar la idea de tu empleado. Como resultado, la eficiencia de tu empresa no mejoró y perdiste la oportunidad de aumentar tu productividad."),
    ("El gobierno ofrece un subsidio para empresas que invierten en energía renovable. ¿Aceptar (A) o Rechazar (R)?", 'A',
     "Rechazaste la oferta de subsidio para invertir en energía renovable. Más tarde, te diste cuenta de que tus competidores aprovecharon la oportunidad para reducir costos y mejorar su imagen."),
    ("Hay una oportunidad de capacitar a los empleados en nuevas habilidades. ¿Capacitar (C) o No invertir (N)?", 'C',
     "Decidiste no invertir en la capacitación de tus empleados. Como resultado, la productividad de tu empresa no mejoró y tus empleados se sintieron desmotivados."),
    ("Tu proveedor principal ha aumentado sus precios. ¿Buscar un nuevo proveedor (B) o Aceptar los nuevos precios (A)?", 'B',
     "Decidiste aceptar los nuevos precios de tu proveedor principal. Esto resultó en una disminución en tus márgenes de ganancia."),
    ("Un competidor está ofreciendo un producto similar a un precio más bajo. ¿Reducir tus precios (R) o Mantenerlos (M)?", 'R',
      "Decidiste mantener tus precios a pesar de la competencia. Como resultado, perdiste una parte de tu base de clientes."),
    ("Tu empresa ha recibido una gran cantidad de críticas negativas en las redes sociales. ¿Responder a las críticas (R) o Ignorarlas (I)?", 'R',
     "Decidiste ignorar las críticas en las redes sociales. Esto resultó en una disminución de la confianza del cliente y una pérdida de reputación.")
]

for _ in range(3):
    situacion, opcion_correcta, mensaje_malo = random.choice(situaciones)
    decision = input(situacion + " ")

    if decision.upper() == opcion_correcta:
        print("Decisión correcta. Ganas puntos de crecimiento.")
        mi_empresa.crecimiento_economico(2)
        respuestas_correctas += 1
    else:
        print("Decisión incorrecta. Pierdes puntos de crecimiento.")
        mi_empresa.crecimiento_economico(-1)
        print(mensaje_malo)

    if random.random() < 0.3:
        print("Ha ocurrido un evento inesperado que afecta negativamente a tu empresa.")
        mi_empresa.crecimiento -= 1

# Contratación del segundo trabajador
if respuestas_correctas >= 1:
    nombre_trabajador = input("Pese a todo la empresa poco a poco sigue creciendo, otra persona llega a pedirte empleo, su nombre es...: ")
    salario_trabajador = float(input(f"Ingrese el salario por hora de {nombre_trabajador}: $"))
    horas_trabajo = int(input(f"Ingrese las horas de trabajo por día de {nombre_trabajador}: "))
    experiencia_trabajador = input(f"Ingrese la experiencia de {nombre_trabajador} (novato, medio, experimentado): ")

    segundo_trabajador = Trabajador(nombre_trabajador, salario_trabajador * horas_trabajo, horas_trabajo, experiencia_trabajador)

    if salario_trabajador * horas_trabajo * 30 < 1000:  # Verifica si el salario mensual es inferior a $1000
        print(f"Lo siento, {nombre_trabajador}, el salario ofrecido es demasiado bajo.")
    else:
        if mi_empresa.condiciones_aptas(segundo_trabajador):
            mi_empresa.contratar(segundo_trabajador)
            print(f"Has contratado a {nombre_trabajador} con un salario de ${segundo_trabajador.salario} por día y trabajará {segundo_trabajador.horas_trabajo} horas por día.")
        else:
            print("No has cumplido con las condiciones laborales mínimas para los trabajadores. El juego no puede continuar.")
            exit()
else:
    print("No has respondido correctamente a suficientes preguntas, por lo que no puedes contratar a más trabajadores por el momento.")

# Segunda tanda de preguntas
for _ in range(3):
    situacion, opcion_correcta, mensaje_malo = random.choice(situaciones)
    decision = input(situacion + " ")

    if decision.upper() == opcion_correcta:
        print("Decisión correcta. Ganas puntos de crecimiento.")
        mi_empresa.crecimiento_economico(1)
        respuestas_correctas += 1
    else:
        print("Decisión incorrecta. Pierdes puntos de crecimiento.")
        mi_empresa.crecimiento_economico(-1)
        print(mensaje_malo)

    if random.random() < 0.3:
        print("Ha ocurrido un evento inesperado que afecta negativamente a tu empresa.")
        mi_empresa.crecimiento -= 1

# Contratación del tercer trabajador
if respuestas_correctas >= 3:
    nombre_trabajador = input("Vaya, ya te estas volviendo conocido, una tercera persona llega a contactarse contigo para que lo contrates, y te recuerda que contratar novatos es importante, su nombre es: ")
    salario_trabajador = float(input(f"Ingrese el salario por hora de {nombre_trabajador}: $"))
    horas_trabajo = int(input(f"Ingrese las horas de trabajo por día de {nombre_trabajador}: "))
    experiencia_trabajador = input(f"Ingrese la experiencia de {nombre_trabajador} (novato, medio, experimentado): ")

    tercer_trabajador = Trabajador(nombre_trabajador, salario_trabajador * horas_trabajo, horas_trabajo, experiencia_trabajador)

    if salario_trabajador * horas_trabajo * 30 < 1000:  # Verifica si el salario mensual es inferior a $1000
        print(f"Lo siento, {nombre_trabajador}, el salario ofrecido es demasiado bajo.")
    else:
        if mi_empresa.condiciones_aptas(tercer_trabajador):
            mi_empresa.contratar(tercer_trabajador)
            print(f"Has contratado a {nombre_trabajador} con un salario de ${tercer_trabajador.salario} por día y trabajará {tercer_trabajador.horas_trabajo} horas por día.")
        else:
            print("No has cumplido con las condiciones laborales mínimas para los trabajadores. El juego no puede continuar.")
            exit()
else:
    print("No has respondido correctamente a suficientes preguntas, por lo que no puedes contratar a más trabajadores por el momento.")
    
# Verificar la condición de empleo decente
if not mi_empresa.verificar_empleo():
    print("Ninguno de tus trabajadores es novato, lo que ha resultado en exceso de carga de trabajo para los experimentados. Los trabajadores se han ido y la empresa no ha generado empleo suficiente.")
    mi_empresa.trabajadores = []  # Todos los trabajadores se van
    exit()

# Mostrar la descripción de todos los trabajadores contratados
print("Descripción de los trabajadores en la empresa:")
mi_empresa.mostrar_trabajadores()

# Añadir un manager y mostrar su descripción
manager_nombre = input("Un manager ha visto tu empresa, y confia en ti para un proyecto, se identifica como...: ")
manager_salario = float(input(f"Ingrese el salario por hora del manager {manager_nombre}: $"))
manager_horas_trabajo = int(input(f"Ingrese las horas de trabajo por día del manager {manager_nombre}: "))
manager_experiencia = input(f"Ingrese la experiencia del manager {manager_nombre} (novato, medio, experimentado): ")
manager = Manager(manager_nombre, manager_salario * manager_horas_trabajo, manager_horas_trabajo, manager_experiencia, mi_empresa.trabajadores)

if salario_trabajador * horas_trabajo * 30 < 1000: 
    print(f"Lo siento, {manager_nombre}, el salario ofrecido es demasiado bajo.")
else:
    if mi_empresa.condiciones_aptas(manager):
        mi_empresa.contratar(manager)
        print(f"Has contratado a un manager: {manager_nombre}")
        print("Descripción del manager y su equipo:")
        print(manager.describir())
    else:
        print("No has cumplido con las condiciones laborales mínimas para los trabajadores. El juego no puede continuar.")
        exit()

# Verificar el final para el dueño de la empresa
if mi_empresa.crecimiento >= 3:
    print("¡La empresa prosperó y tiene un mejor rendimiento! Has logrado entender correctamente la importancia de generar" , "\n" ,
    "empleo tanto para los empresarios como los propios trabajadores. Lograste comprender esto y tu empresa fue creciendo poco a poco, y cumplio con el ODS 8" ,  "\n" ,
    "(trabajo decente y crecimiento económico)")
else:
    print("No has logrado entender que el generar empleo digno, y tomar buenas decisiones pensando en tus empleados y en ti, llevarian a la perdicion cualquier empresa" , "\n" ,
    "tu propia empresa ha caido en quiebra por no pensar en el empleo digno, y no cumplir con el ODS8, lo siento, vuelve a intentarlo")