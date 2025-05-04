import datetime

class Fechas:
    def __init__(self, nombre, fecha_nacimiento, altura):
        self.nombre = nombre
        self.fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        self.altura = altura

    def __float__(self):
        return float(self.altura)

    def edad(self):
        hoy = datetime.date.today()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def edad_persona(self):
        if self.edad() >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} es menor de edad")

    def crecer(self, cm):
        if cm < 0 or cm > 50:
            print(f"Error: {self.nombre} no puede crecer {cm} cm. Debe ser entre 0 y 50 cm.")
        else:
            metros = cm / 100
            self.altura += metros
            print(f"{self.nombre} ha crecido {cm} cm. Ahora mide {self.altura:.2f} m")

    def cumple_hoy(self):
        hoy = datetime.date.today()
        return hoy.month == self.fecha_nacimiento.month and hoy.day == self.fecha_nacimiento.day

    def dias_para_cumple(self):
        hoy = datetime.date.today()
        proximo = datetime.date(hoy.year, self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        if proximo < hoy:
            proximo = datetime.date(hoy.year + 1, self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        return (proximo - hoy).days

    def __str__(self):
        return f"{self.nombre} {self.edad()} años {self.altura:.2f} m"


s1 = Fechas("Kimberly", "2006-07-24", 1.70)
s2 = Fechas("Juan", "2008-01-14", 1.90)
s3 = Fechas("Sergio", "2006-12-06", 1.69)
s4 = Fechas("Fredy", "1945-02-12", 1.72)
s5 = Fechas("Yes", "2000-09-19", 1.60)

personas = [s1, s2, s3, s4, s5]


for persona in personas:
    print(f"Hola, mi nombre es {persona.nombre} y tengo {persona.edad()} años")
    persona.edad_persona()
    persona.crecer(5)

    if persona.cumple_hoy():
        print(f"¡Hoy es el cumpleaños de {persona.nombre}!")
    else:
        print(f"Faltan {persona.dias_para_cumple()} días para el cumpleaños de {persona.nombre}")
    
    print(persona) 
    print()