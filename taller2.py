import random
class carta_trebol:
    def __init__ (self,numero,palo):
        self.numero = numero
        self.palo = palo
    def __str__(self):
        return f"carta {self.numero} del palo {self.palo}"
b = [] 
for i in range (1,14):
    t = carta_trebol(i,"trebol")
    b.append(t)
for t in b:
    print(t)
class carta_diamante:
    def __init__ (self,numero,palo):
        self.numero = numero
        self.palo = palo
    def __str__(self):
        return f"carta {self.numero} del palo {self.palo}"
b = [] 
for i in range (1,14):
    t = carta_diamante(i,"diamante")
    b.append(t)
for t in b:
    print(t)
class carta_pica:
    def __init__ (self,numero,palo):
        self.numero = numero
        self.palo = palo
    def __str__(self):
        return f"carta {self.numero} del palo {self.palo}"
b = [] 
for i in range (1,14):
    t = carta_pica(i,"pica")
    b.append(t)
for t in b:
    print(t)
class carta_corazon:
    def __init__ (self,numero,palo):
        self.numero = numero
        self.palo = palo
    def __str__(self):
        return f"carta {self.numero} del palo {self.palo}"
b = [] 
for i in range (1,14):
    t = carta_corazon(i,"corazon")
    b.append(t)
for t in b:
    print(t)
palos = ['corazones', 'diamantes', 'tréboles', 'picas']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']
baraja = []
for palo in palos:
    for valor in valores:
        baraja.append((valor, palo))

random.shuffle(baraja)

print(baraja)