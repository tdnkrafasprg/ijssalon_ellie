from helper import *
from presentatie import *
import csv

inkomsten = {
"Aardbeien-ijs-totaal" : int("1000"),
"Vanille-ijs-totaal" : int("2000"),
"Chocolade-ijs-totaal" : int("1500"),
"Waterijsjes-totaal" : int("750")
}

totaal_inkomsten = som(inkomsten)

presenteren = presenteer(inkomsten,totaal_inkomsten)

with open('boekhouding.csv', 'w', newline=") as csvfile:
    for key, value in inkomsten.items():
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([key,value])