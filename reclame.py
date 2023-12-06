def aanbieding_1(smaak,prijs,korting):
    aanbieding = prijs - (prijs * korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {aanbieding} euro."
    return uitvoer

def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    btw_bedrag = btw * totaal
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer

def laag_en_hoog(mijn_lijst):
    Max = max(mijn_lijst)
    Min = min(mijn_lijst)
    return Max, Min

def gemiddelde(mijn_lijst):
    Average = sum(mijn_lijst) / len(mijn_lijst)
    Uitvoer = f"De gemiddelde inkomsten deze week zijn {Average} euro."
    return Uitvoer

mijn_lijst = 220, 430, 125, 160, 205, 90, 345
print(gemiddelde(mijn_lijst))
          