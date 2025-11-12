from veicolo import Veicolo
class Moto(Veicolo):
    def __init__(self, marca, modello, cilindrata, peso, costo, capienza_borse):
        super().__init__(marca, modello, cilindrata, peso, costo)
        self.capienza_borse = capienza_borse

    def __str__(self):
        return f"Moto: {self.marca}, modello: {self.modello}, cilindrata: {self.cilindrata}cc, peso: {self.peso}kg, costo: {self.costo}€, capienza borse da viaggio: {self.capienza_borse}cm"

moto1 = Moto("Ducati", "Multistrada", 1200, 210, 18000, 50)
moto2 = Moto("BMW", "R1250GS", 1250, 249, 22000, 60)
moto3 = Moto("Honda", "Africa Twin", 1100, 240, 17000, 55)
moto4 = Moto("Yamaha", "Tracer 9 GT", 890, 214, 14000, 45)
#moto5 TODO
lista_moto = [moto1, moto2, moto3, moto4]

for moto in lista_moto:
    print(moto)