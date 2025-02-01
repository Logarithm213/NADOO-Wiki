# Dies ist ein Beispielskript mit verschiedenen Bugs und Grundkonzepten der Python-Programmierung

# Variablen: Behälter für Daten
zahl = 10
kommazahl = 3.14
text = "Hallo, Welt!"
liste = [1, 2, 3, 4, 5]

# Funktionen: Wiederverwendbare Codeblöcke
# Bug 1: Fehlender Doppelpunkt nach der Funktionsdefinition
def addiere(a, b):
    # Bug 2: Falsche Einrückung
  return a + b

# Kontrollstrukturen: Steuern den Programmablauf
# If-Anweisung: Bedingte Ausführung von Code
# Bug 3: Falscher Vergleichsoperator
if zahl == 10:
    print("Die Zahl ist 10")
else:
    print("Die Zahl ist nicht 10")

# For-Schleife: Iteration über eine Sequenz
# Bug 4: Fehlender Doppelpunkt nach der for-Schleife
# Bug 5: Verwendung einer nicht definierten Variable
for i in range(5):
    print(i)

# While-Schleife: Wiederholung, solange eine Bedingung wahr ist
# Bug 6: Endlosschleife
x =  0

while x < 5:
    print("Dies ist eine Endlosschleife")
    x += 1
# Klassen: Blaupausen für Objekte
class Auto:
    # Bug 7: Fehlender self-Parameter
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell
    
    # Bug 8: Falsche Methodendefinition
    def fahren(self):
        print(f"{self.marke} {self.modell} fährt.")

# Fehlerbehandlung: Umgang mit Ausnahmen
# Bug 9: Falsche Ausnahmebehandlung
try:
    resultat = 10 / 0
except:
    print("Ein Fehler ist aufgetreten")
finally:
    print("Dies wird immer ausgeführt")

# Hauptprogramm
if __name__ == "__main__":
    # Bug 10: Falscher Funktionsaufruf
    ergebnis = addiere(5, 9)
    print(f"Das Ergebnis ist: {ergebnis}")

    # Objekterstellung und -verwendung
    mein_auto = Auto("VW", "Golf")
    mein_auto.fahren()

print("Programm beendet")