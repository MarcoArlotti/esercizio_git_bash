class Veicolo:
    def __init__(self, marca, modello, cilindrata, peso, costo):
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilindrata
        self.peso = peso
        self.costo = costo

class Auto(Veicolo):
    def __init__(self, marca, modello, cilindrata, peso, costo, aria_condizionata, radio):
        super().__init__(marca, modello, cilindrata, peso, costo)
        self.aria_condizionata = aria_condizionata
        self.radio = radio

    def __str__(self):
        return f"Auto: {self.marca}, modello: {self.modello}, cilindrata: {self.cilindrata}cc, peso: {self.peso}kg, costo: {self.costo}€, aria condizionata: {self.aria_condizionata}, radio: {self.radio}"

auto1 = Auto("Fiat", "Panda 4x4", 1200, 950, 12000, False , False)
auto2 = Auto("Ferrari", "488 Spider", 3900, 1520, 250000, True, True)
auto3 = Auto("Volkswagen", "polo", 1600, 1300, 22000, True, True)
auto4 = Auto("Ducati", "Monster", 1100, 180, 15000, True, True)
auto5 = Auto("Tesla", "cybertruck", 0, 1625, 4500, True, True)

lista_auto = [auto1, auto2, auto3, auto4, auto5]

for auto in lista_auto:
    print(auto)
