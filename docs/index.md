---
# Angaben fürs Deckblatt
title: Studienleistung zur Rekursion
subtitle: Fachdidaktik 2 GymInf FS24
author: Jacques Mock Schindler
date: 15. Februar 2024
institute: Universität Fribourg
# Einstellungen für die Erstellung eines PDF
output:
  pdf_document:
    latex_engine: xelatex
fontsize: 12pt
papersize: a4
lang: de-CH
# Angaben zur Bibliographie
bibliography: ../data/Studienleistung4.bib       # Aus Zotero exportiertes Datenbankfile
csl: ../data/chicago-fullnote-bibliography-short-title-subsequent.csl       # Darstellung der bibliographischen Angaben
---

# Eine Fehlvorstellung zur Rekursion

Rekursion ist eine fortgeschrittene Programmiertechnik. Python stellt
verhältnismässig einfache Schleifenkonstruktionen zur Verfügung. Aus
diesem Grund sind Implementationen unter Verwendung von Rekursionen in
Python relativ selten.  
Trotzdem ist die Rekursion eine nützliche Technik die man kennen sollte
\- nicht zu Letzt, um über Strukturen mit unvorhersehbaren Formen und
Tiefen zu iterieren[@lutzLearningPython2013, p. 555].

Weil rekursiv implementierte Funktionen in der Praxis nicht so häufig
sind und trotzdem für wesentliche Aufgaben ein nützliches Hilfsmittel
darstellen, lohnt es sich, sich mit Fehlvorstellungen im Zusammenhang
mit der rekursiven Implementierung von Funktionen auseinanderzusetzen.  

## Die Gausssche Summenformel als Anwendungsfall für die Entstehung von Fehlvorstellungen

Eine wesentliche Fehlvorstellung soll anhand der Gaussschen Summenformel
(kleiner Gauss) illustriert werden. Die Gausssche Summenformel dient zur
addition der ersten n aufeinanderfolgenden natürlichen Zahlen:

$$
1+2+3+4+\dots+n = \sum_{k=1}^{n} k = \frac{n(n+1)}{2}=\frac{n^2+n}{2}
$$

### Fachdidaktische Perspektive

Im Mathematikunterricht wird die Gausssche Summenformel oft dazu
verwendet, den Beweis durch vollständige Induktion zu üben.
Induktionsbeweise haben eine grosse Ähnlichkeit zu
Rekursion[@leeDataStructuresAlgorithms2024, p. 74]. Diese Ähnlichkeit
kann einem dazu verleiten, eine rekursive Implementation für besonders
Effizient zu halten.

### Fachliche Perspektive

Wenn rekursive Definitionen mathematischer Phänomene vorliegen, sind
diese sehr einfach als Funktion zu implementieren. Dabei kann allerdings
vergessen gehen, dass diese Einfachheit einen Preis in der Form eines
hohen Speicherbedarfs hat.