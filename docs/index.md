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
verhältnismässig einfache Schleifenkonstruktionen zur Verfügung stellt,
sind Implementationen unter Verwendung von Rekursionen in
Python relativ selten.  
Trotzdem ist die Rekursion eine nützliche Technik, die man kennen sollte
\- nicht zu Letzt, um über Strukturen mit unvorhersehbaren Formen und
Tiefen zu iterieren[@lutzLearningPython2013, p. 555].

Weil rekursiv implementierte Funktionen in der Praxis nicht so häufig
sind, und trotzdem für wesentliche Aufgaben ein nützliches Hilfsmittel
darstellen, lohnt es sich, Fehlvorstellungen im Zusammenhang
mit der rekursiven Implementierung von Funktionen aufzudecken und
richtig zu stellen.  

## Die Gausssche Summenformel als Anwendungsfall für die Entstehung von Fehlvorstellungen

Eine wesentliche Fehlvorstellung soll anhand der Gaussschen Summenformel
(kleiner Gauss) illustriert werden. Die Gausssche Summenformel dient zur
addition der ersten n aufeinanderfolgenden natürlichen Zahlen:

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
üben. Daraus ergibt sich aus *fachdidaktischer Perspektive* das Problem,
dass die vollständige Induktion der Rekursion ähnlich 
sieht[@leeDataStructuresAlgorithms2024, p. 74]. Daraus ergibt sich dann
die Fehlvorstellung, dass eine rekursive Implementation der Gaussschen
Summenformel eine gegenüber der direkten Implementation überlegene
Lösung sei.

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
   def gaus_rec(n : int) -> int:
       if n == 1:    # Basisfall
           return 1 
       else:         # Rekursionsfall
           return n + gaus_rec(n - 1) 
   ```

## Literatur

