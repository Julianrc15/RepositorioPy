class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")


merlin=Mago()
ashe=Arquero()
shen=Samurai()

personajes=[ashe, merlin, shen]

for personaje in personajes:
    print(personaje.atacar())


class Mago():
    def atacar(self):
        print("Ataque mágico")
 
class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
 
class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
gandalf = Mago()
hawkeye = Arquero()
jack = Samurai()
 
personajes = [hawkeye, gandalf, jack]
 
for personaje in personajes:
    personaje.atacar()





