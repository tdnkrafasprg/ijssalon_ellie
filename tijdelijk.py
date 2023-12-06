from helper import decoreer

def print_aanbieding():
    IJssalon_start = {
        "aardbei" : "3",
        "vanille" : "4",
        "chocolade" : "5"
    }
    Aanbieding = int(IJssalon_start["vanille"])*0.8
    reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {Aanbieding}")
    reclame_tekst2 = reclame_tekst.upper()
    reclame_tekst3 = reclame_tekst2.split()
    for el in reclame_tekst3:
        if len(el) > 4:
            print(el.upper())
        else:
            print(el.lower())
decoreer("Aanbieding")
print_aanbieding()
