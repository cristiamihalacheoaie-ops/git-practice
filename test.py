class TransportExpress(StrategieTransport):
    def calculeaza_cost(self,comanda:Comanda) -> float:
        return 20 + 0.8*comanda.distanta_km + 1.8* comanda.greutate_kg

# De ce metodele abstracte sunt de tipul pass
class CalculatorTransport:
    def __init__(self, strategie:StrategieTransport):
        self.strategie = strategie
    def seteaza_strategia(self, strategie:StrategieTransport):
        self.strategie = strategie
    def cost(self,comanda:Comanda) -> float:
        return round(self.strategie.calculeaza_cost(comanda),2)

c = Comanda(greutate_kg=4, distanta_km=25,valoare_lei=300)
calculam = CalculatorTransport(TransportStandard())
print(calculam.cost(c))
calculam.seteaza_strategia(TransportExpress())
print(calculam.cost(c))