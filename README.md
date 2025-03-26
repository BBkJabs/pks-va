# Python: Variablen und Datentypen

## Python Grundlagen
Wie in der Mathematik gibt es auch in der Programmierung "Variablen". 

### Datentypen
In der Programmierung unterscheidet man dabei unterschiedliche "Datentypen". In Python gibt es unter anderem folgende Basis-Datentypen:  
- Ganzzahlen                  (integer)
- Kommazahlen                 (float)
- Wahrheitswert               (bool)
- Zeichenketten               (string)  

### Zuweisung
Um nun einer Variablen einen Inhalt zuzuweisen, benötigt man den Zuweisungs-Operator '='. Dabei steht immer LINKS vom Gleichheitszeichen die Variable, der ein Inhalt zugewiesen werden soll und RECHTS vom Gleichheitszeichen steht der Inhalt, der in der Variablen abgelegt werden soll:            
```
zahl1 = 4           # integer
zahl2 = 12.7        # float
istRichtig = True   # bool
text  = "Hallo"     # string
```
**WICHTIG: Variablennamen sollten mit einem Kleinbuchstaben beginnen!!!**

### Datentyp anzeigen
Man kann sich den Datentyp einer Variablen durch die Anweisung "type" anzeigen lassen:  
```
print(type(zahl1))      # INT_eger
print(type(zahl2))      # FLOAT
print(type(istRichtig)) # BOOL
print(type(text))       # STR_ing
```

### Rechnen mit (Zahl-)Variablen
Mit (Zahlen-)Variablen kann man rechnen und man kann den Inhalt von Variablen ausgeben:  
```
ergebnis = zahl1 + zahl2
print(ergebnis)
```

Variablenwerte können sich im Laufe des Programms ändern:
```
zahl2 = 9
ergebnis = 3 * zahl2 
print(ergebnis)
zahl2 = 6.7
ergebnis = zahl1 + zahl2
print(ergebnis)
```

In der folgenden Zeile wird zunächst der Term rechts vom Zuweisungs-Operator berechnet (6.7 + 0.3) und dann das Ergebnis in die Variable links vom Zuweisungs-Operator (zahl2) gespeichert:
```
zahl2 = zahl2 + 0.3
print(zahl2)
```

Die Variable "zahl1" wird nun implizit zu einer Textvariablen umgewandelt. Allerdings ist der Variablenname jetzt nicht mehr gut gewählt ;)
```
zahl2 = "Nun ist in der Variablen ein Text gespeichert."
print(zahl2)
```


### Texte "addieren"
Neben Zahlen können auch Texte "addiert", also kombiniert, werden:
`print("Hallo " + "Welt!")`

Folgende Zeile ist nicht möglich, da sich Text und Zahlen NICHT kombinieren lassen:
`print("Zahl Vier: " + zahl2)`

Dafr würde folgende Möglichkeit funktionieren (siehe Kapitel "Umwandlungen"):
`print("Zahl Vier: " + str(zahl2))`

### Umwandlungen
Durch eine explizite Umwandlung kann eine Zahl in einen string (oder umgekehrt) umgewandelt werden:
```
zahl = 4
text = "9"
print("Zahl Vier: " + str(zahl))                       # str steht für string und damit eine Umwandlung in einen string
print("Typ von Variable zahl: " + str(type(zahl1)))    # Hier wird der Datentyp von "zahl1" ermittelt und dann als Zeichenkette (String) angezeigt
print(5 * int(text))                                   # Hier wird der Text "9" in eine Ganzzahl (int) umgewandelt, mit 5 multipliziert und dann ausgegegen
```

## Aufgabe
Ändere das Python Skript in der Datei variablesAndDatatypes. Lege 4 Variablen mit 4 verschiedenen Datentyen (string, bool, integer, float) an:
- Variable "ganzzahl" mit Wert 42
- Variable "kommazahl" mit Wert 3.14
- Variable "istPythonDoof" mit Wert False
- Variable "text" mit Wert 'Ich mag Python'  

Anschließend soll mit den Anweisungen "print", "type" und "str" der Variablenname, der Variablenwert und der Variablen-Datentyp jeweils in einem Satz ausgegeben werden. 

Beispiel der ersten Ausgabezeile:  
*Die Variable 'ganzzahl' ist vom Datentyp '<class 'int'>' und hat gespeichert: 42*

**WICHTIG:** Ändere **NICHT** die anderen Dateien
