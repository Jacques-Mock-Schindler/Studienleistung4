---
# Angaben fürs Deckblatt
title: Studienleistung zur Rekursion
subtitle: Fachdidaktik 2 GymInf FS24
author: Jacques Mock Schindler
date: 17. Februar 2024
institute: Universität Fribourg
# Einstellungen für die Erstellung eines PDF
header-includes:
    - \usepackage{amsmath}
output:
  pdf_document:
    latex_engine: xelatex
fontsize: 11pt
papersize: a4
lang: de-CH
# Angaben zur Bibliographie
bibliography: ../data/Studienleistung4.bib       # Aus Zotero exportiertes Datenbankfile
csl: ../data/chicago-fullnote-bibliography-short-title-subsequent.csl       # Darstellung der bibliographischen Angaben
# pandoc-Befehl: pandoc --citeproc -s --from Markdown --to pdf -o xxx.pdf input.md
---

# Ausgangslage

Rekursion ist eine fortgeschrittene Programmiertechnik. Weil Python 
mächtige und flexible Schleifenkonstruktionen zur Verfügung stellt,
werden in Python rekursive Lösungen vor allem verwendet, um über
Strukturen mit unvorhersehbaren Formen und Tiefen zu
iterieren[^1]. Daher ist die Rekursion eine
nützliche Technik, die man kennen muss.

Weil rekursiv implementierte Funktionen eine fortgeschrittenere Lösung
für Probleme darstellen, und vor allem für anspruchsvollere Aufgaben ein
nützliches Hilfsmittel sind, lohnt es sich, Fehlvorstellungen im
Zusammenhang mit der rekursiven Implementierung von Funktionen
aufzudecken und richtig zu stellen.  

## Die Gausssche Summenformel als Anwendungsfall für die Entstehung von Fehlvorstellungen

Eine wesentliche Fehlvorstellung bezieht sich auf den Speicherbedarf von
rekursiv implementierten Lösungen. Dies soll anhand der Gaussschen
Summenformel (kleiner Gauss) illustriert werden. Die Gausssche
Summenformel dient zur Addition der ersten $n$ aufeinanderfolgenden
natürlichen Zahlen: 

$$
1+2+3+4+\dots+n = \sum_{k=1}^{n} k = \frac{n(n+1)}{2}=\frac{n^2+n}{2}
$$

Natürlich ist es möglich, die Gausssche Summenformel direkt als

```Python
def gauss_direkt(n):
    return (n ** 2 + n) / 2
```

zu implementieren.  

Allerdings wird im Mathematikunterricht die Gausssche Summenformel
gelegentlich dazu verwendet, den Beweis durch vollständige Induktion zu
üben.  
Lee und Hubbard weisen in ihrem Lehrbuch zu Recht auf die Ähnlichkeiten
der vollständigen Induktion und der Rekursion
hin[^2]. Daraus ergibt sich aus
*fachdidaktischer Perspektive* das Problem, dass die Schüler und
Schülerinnen (SuS) eine rekursive Implementation der Gaussschen
Summenformel für eine gegenüber der direkten Implementation überlegene
Lösung halten könnten.

Unter *fachlichen Gesichtspunkten* ist die Implementierung der
Gaussschen Summenformel, zumindest dann wenn die entsprechende
Definition wie unten als Formel vorliegt[^3], 
verhältnismässig einfach.

$$
\sum_{k=1}^{n}k=
\left\{
    \begin{array}{lll}
        1,&n=1&\text{Basisfall}\\
        n+\sum\limits_{k=1}^{n-1}k,&\forall n > 1&\text{Rekursionsfall}
    \end{array}
\right.
$$

Allerdings darf darob nicht vergessen werden, dass rekursive Lösungen
bezüglich des erforderlichen Speicherplatzes und Rechenaufwandes "teuer"
sind. Dies gilt auch dann, wenn wie hier die Beanspruchung des call
stack "nur" proportional zur Rekursionstiefe (dh. zu $n$) wächst. Der
"Preis" wird umso deutlicher, wenn der Speicherbedarf demjenigen der
direkten Implementation gegenübergestellt wird. In der direkten
Implementation ist der Speicherbedarf und Rechenaufwand konstant.

Man läuft bei rekursiv implementierten Funktionen damit Gefahr, den für
die entsprechende Lösung erforderlichen Speicherplatz zu unterschätzten.


## Aufgabe

Mit der folgenden Aufgabenstellung soll das Bewusstsein für diese
Fehlvorstellung geschärft werden. Die Aufgabe besteht
aus zwei Teilaufgaben. In der Teilaufgabe a) soll die Gausssche
Summenformel rekursiv und in Teilaufgabe b) direkt implementiert werden.  
In beiden Teilaufgaben soll der *call stack* durch den Aufruf
entsprechender print() Funktionen sichtbar gemacht werden.

Die Aufgabenstellung wird als 
[Jupyter Notebook](https://colab.research.google.com/github/Jacques-Mock-Schindler/Studienleistung4/blob/main/src/rekursion_sus.ipynb)
abgegeben. Die
Musterlösung wird auftragsgemäss als 
[ausführbare .py Datei](https://github.com/Jacques-Mock-Schindler/Studienleistung4/blob/main/src/rekursion_muloe.py)
eingereicht.
Der ausführliche Kommentar zur Musterlösung wird hier noch in Textform
zur Verfügung gestellt. Die Kommentare im Code richten sich an die SuS
und entsprechen nicht den Vorgaben von PEP 8.

### Kommentar zur rekursiven Implementation

1. Die rekursive Variante der Gaussschen Summenformel wird in
   einem ersten Schritt noch ohne die verlangten print() Funktionen
   implementiert. Sie bildet exakt die rekursive Definition der
   Gaussschen Summenformel ab.

   ```Python
   def gauss_rec(n : int) -> int:
       if n == 1:    # Basisfall
           return 1 

       else:         # Rekursionsfall
           return n + gauss_rec(n - 1) 
   ```

2. In einem zweiten Schritt werden die print() Funktionen im Basisfall
   eingefügt. Aus typographischen Gründen wird der Aufruf der print()
   Funktion auf mehrere Zeilen verteilt. Aus Gründen der Lesbarkeit wird
   auch der zweite Satz als f-string formatiert, auch wenn dies nicht
   nötig wäre.

   ```Python
   def gauss_rec(n : int) -> int:
       if n == 1:    # Basisfall
           print(
            f'Der aktuelle Wert von n ist {n}. '
            f'Basisfall erreicht!'
            )           
           return 1 

       else:         # Rekursionsfall
           return n + gauss_rec(n - 1) 
   ```

3. Im letzten Schritt werden die print() Funktionen im Rekursionsfall
   eingefügt. Dies ist etwas schwieriger, weil es solche vor dem
   Eintreten in eine neue Rekursionsebene und solche nach deren
   Verlassen braucht. Dazu muss das Resultat des Rekursionsfalls einer
   eigenen Variablen zugewiesen werden. Die Variable kann dann
   ihrerseits nach dem Aufruf der print() Funktion mit dem return
   Statement zurückgegeben werden. So ist es möglich, die print()
   Funktionen vor und nach dem Rekursionsaufruf zu platzieren.

   ```Python
   def gauss_rec(n : int) -> int:
       if n == 1:    # Basisfall
           print(
                f'Der aktuelle Wert von n ist {n}. '
                f'Basisfall erreicht!'
                )
           return 1 

       else:         # Rekursionsfall
           # Ausgaben vor dem Rekursionsaufruf
           print(
            f'Es sind noch {n} Rekursionen nötig, '
            f'dies entspricht dem \n aktuellen Wert von n '
            f'(der call stack ist noch im Aufbau).'
            )
           # Rekursionsaufruf
           resultat = n + gauss_rec(n-1)
           # Ausgaben nach dem Rekursionsaufruf
           print(
            f'Der aktuelle Wert von n ist {n} '
            f'und das Zwischenergebnis {resultat} \n'
            f'(der call stack wird abgebaut).'
            )
           return resultat
    ```

Die solcherart mit print() Funktionen ergänzte Implementation führt bei
einem Aufruf `print(gauss_rec(3))` zu folgender Ausgabe:

```bash
Es sind noch 3 Rekursionen nötig, dies entspricht dem 
 aktuellen Wert von n (der call stack ist noch im Aufbau).
Es sind noch 2 Rekursionen nötig, dies entspricht dem 
 aktuellen Wert von n (der call stack ist noch im Aufbau).
Der aktuelle Wert von n ist 1. Basisfall erreicht!
Der aktuelle Wert von n ist 2 und das Zwischenergebnis 3 
(der call stack wird abgebaut).
Der aktuelle Wert von n ist 3 und das Zwischenergebnis 6 
(der call stack wird abgebaut).
6
```

### Kommentar zur direkten Implementation

Dem steht die direkte Implementation gegenüber. Auch in der direkten
Implementation wurde eine print() Funktion eingebaut.

```Python
def gauss_direct(n : int) -> int:
    print(f'Der aktuelle Wert von n ist {n}.')
    return int((n * (n + 1)) / 2)
```

Der Aufruf von `print(gauss_direct(3))` führt zu folgender Ausgabe:

```bash
Der aktuelle Wert von n ist 3.
6
```

Dies zeigt den grösseren Speicher- und Rechenbedarf der rekursiven Implementation
deutlich. 


## Literatur

[^1]: Lutz, Mark. Learning Python. Fifth edition. Beijing, Cambridge,
    Farnham, Köln, Sebastopol, Tokyo: O’Reilly, 2013. p. 555.

[^2]: Lee, Kent D., und Steve Hubbard. Data Structures and Algorithms
    with Python: With an Introduction to Multiprocessing. Second
    edition. Cham: Springer, 2024. p. 74.

[^3]: Inden, Michael. Python Challenges: 100 Proven Programming Tasks
    Designed to Prepare You for Anything. New York: Apress, 2022. p. 74;
    Lee und Hubbard (ibd.). pp. 75.
