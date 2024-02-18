def gauss_rec(n : int) -> int:
    """Rekursive Implementation der Gaussschen Summenformel

    Diese Funktion berechnet die Summe der ersten n natürlichen Zahlen. Sie
    zeigt mit den verschiedenen print() Funktionen, wie der call stack auf-
    und wieder abgebaut wird.

    Args:
        n (int): Die natürliche Zahl bis und mit welcher die Summe
        gebildet wird.

    Returns:
        Die Summe aller n natürlichen Zahlen als natürliche Zahl.
    """

    # Basisfall
    if n == 1:
        print(
            f'Der aktuelle Wert von n ist {n}. '
            f'Basisfall erreicht!'
            )
        return 1

    else:
        # Die folgende print() Funktion wird aufgerufen,
        # bevor die nächste Rekursionsebene erreicht wird
        print(
            f'Es sind noch {n} Rekursionen nötig, '
            f'dies entspricht dem \n aktuellen Wert von n '
            f'(der call stack ist noch im Aufbau).'
            )
        # Rekursionsfall
        resultat = n + gauss_rec(n-1)
        # Die print() Funktion wird aufgerufen, nachdem die
        # vorangegangene Rekursionsebene wieder veralssen worden ist
        print(
            f'Der aktuelle Wert von n ist {n} '
            f'und das Zwischenergebnis {resultat} \n'
            f'(der call stack wird abgebaut).'
            )

        return resultat

def gauss_direct(n : int) -> int:
    """Direkte Implementierung der Gaussschen Summenformel

    Diese Funktion berechnet die Summe der ersten n natürlichen Zahlen.

    Args:
        n (int): Die natürliche Zahl bis und mit welcher die Summe
        gebildet wird.

    Returns:
        Die Summe aller n natürlichen Zahlen als natürliche Zahl.
    """

    print(f'Der aktuelle Wert von n ist {n}.')
    return int((n * (n + 1)) / 2)

def main():
    n = 5
    print(f'Die Summe der ersten {n} natürlichen Zahlen beträgt')
    print(' ')
    print(f'über die rekursive Funktion: {gauss_rec(n)}')
    print(' ')
    print(f'über die direkte Funktion: {gauss_direct(n)}')
    
if __name__ == '__main__':
    main()