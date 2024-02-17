---
# Angaben fürs Deckblatt
title: Studienleistung zur Rekursion
subtitle: Fachdidaktik 2 GymInf FS24
author: Jacques Mock Schindler
date: 16. Februar 2024
institute: Universität Fribourg
# Einstellungen für die Erstellung eines PDF
header-includes:
    - \usepackage{amsmath}
output:
  pdf_document:
    latex_engine: xelatex
fontsize: 12pt
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
iterieren[@lutzLearningPython2013, p. 555]. Daher ist die Rekursion eine
nützliche Technik, die man kennen muss.

Weil rekursiv implementierte Funktionen eine fortgeschrittenere Lösung
für Probleme darstellen, und vor allem für anspruchsvollere Aufgaben ein
nützliches Hilfsmittel darstellen, lohnt es sich, Fehlvorstellungen im
Zusammenhang mit der rekursiven Implementierung von Funktionen
aufzudecken und richtig zu stellen.  

## Die Gausssche Summenformel als Anwendungsfall für die Entstehung von Fehlvorstellungen

Eine wesentliche Fehlvorstellung bezieht sich auf den Speicherbedarf von
rekursiv implementierten Lösungen. Dies soll anhand der Gaussschen
Summenformel (kleiner Gauss) illustriert werden. Die Gausssche
Summenformel dient zur addition der ersten $n$ aufeinanderfolgenden
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
Lee und Hubbard weisen in ihrem Lehrbuch zu recht auf die Ähnlichkeiten
der vollständigen Induktion und der Rekursion
hin[@leeDataStructuresAlgorithms2024, p. 74]. Daraus ergibt sich aus
*fachdidaktischer Perspektive* das Problem, dass eine rekursive
Implementation der Gaussschen Summenformel für eine gegenüber der
direkten Implementation überlegene Lösung gehalten wird.

Unter *fachlichen Gesichtspunkten* ist die Implementierung der
Gaussschen Summenformel, zumindest dann wenn die entsprechende
Definition vorliegt[@indenPythonChallenges1002022, p. 74;
@leeDataStructuresAlgorithms2024, pp. 75], 
recht einfach.

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
bezüglich des erforderlichen Speicherplatzes "teuer" sind. Dies gilt
auch dann, wenn wie hier die Beanspruchung des call stack "nur"
proportional zur Rekursionstiefe (dh. zu $n$) wächst. Der "Preis" wird
umso deutlicher, wenn der Speicherbedarf demjenigen der direkten
Implementation gegenübergestellt wird. In der direkten Implementation
ist der Speicherbedarf konstant.

Man läuft bei rekursiv implementierten Funktionen damit Gefahr, den für
die entsprechende Lösung erforderlichen Speicherplatz zu unterschätzten.


## Aufgabe

Mit der folgenden Aufgabenstellung soll das Bewusstsein für diese
Fehlvorstellung geschärft werden. Aus diesem Grund besteht die Aufgabe
aus zwei Teilaufgaben. In der Teilaufgabe a) soll die Gausssche
Summenformel rekursiv und in Teilaufgabe b) direkt implementiert werden.  
In beiden Teilaufgaben soll der *call stack* durch den Aufruf
entsprechender print() Funktionen sichtbar gemacht werden.

Die Aufgabenstellung wird als Jupyter Notebook abgegeben. Das gleiche
gilt für eine ausführbare Musterlösung. Der ausführliche Kommentar zur
Musterlösung wird hier noch in Textform zur Verfügung gestellt.

1. Die rekursive Variante der Gaussschen Summenformel wird in
   einem ersten Schritt noch ohne die verlangten print() Funktionen
   implementiert.  

   ```Python
   def gauss_rec(n : int) -> int:
       if n == 1:    # Basisfall
           return 1 

       else:         # Rekursionsfall
           return n + gaus_rec(n - 1) 
   ```

2. In einem zweiten Schritt werden die print() Funktionen im Basisfall
   eingefügt. 

   ```Python
   def gauss_rec(n : int) -> int:
       if n == 1:    # Basisfall
           print(f'Der aktuelle Wert von n ist {n}.', end=' ')
           print('Basisfall erreicht!')           
           return 1 

       else:         # Rekursionsfall
           return n + gaus_rec(n - 1) 
   ```

3. Im letzten Schritt werden die print() Funktionen im Rekursionsfall
   eingefügt. Dies ist etwas schwieriger, weil es solche vor dem
   Eintreten in eine neue Rekursionsebene und solche nach derem
   Verlassen braucht. Dazu muss das Resultat des Rekursionsfall einer
   eigenen Variablen zugewiesen werden, die dann ihrerseits
   zurückgegeben werden kann. Dies ermöglicht es, die print() Funktionen
   vor und nach dem Rekursionsaufruf zu platzieren.

   ```Python
   def gauss_rec(n : int) -> int:
       if n == 1:    # Basisfall
           print(f'Der aktuelle Wert von n ist {n}.', end=' ')
           print('Basisfall erreicht!') 
           return 1 

       else:         # Rekursionsfall
           # Ausgaben vor dem Rekursionsaufruf
           print(f'Es sind noch {n} Rekursionen nötig,', end=' ')
           print('dies entspricht dem aktuellen Wert von n', end=' ')
           print('(der call stack ist noch im Aufbau).')
           # Zuweisung des Resultates des Rekursionsaufrufs 
           # an eine eigene Variable
           resultat = n + gauss_rec(n-1)
           # Ausgaben nach dem Rerusionsaufruf
           print(f'Der aktuelle Wert von n ist {n}', end='')
           print(f' und das Zwischenergebnis {resultat}', end=' ')
           print('(der call stack wird abgegebaut).')
           return resultat
    ```

## Literatur

