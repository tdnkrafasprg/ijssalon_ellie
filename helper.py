def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag / personen
    return f"De fooi is {bedrag_pp} per persoon"

def onderstreep(tekst=""):    
    uit = []    
    uit.append(tekst)    
    uit.append(len(tekst) * "=")    
    return uit

def som(ink):
    return sum(ink.values())