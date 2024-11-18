# https://dodona.be/nl/courses/4195/series/46776/activities/1225527836


class Bifid:
    def __init__(self, n, symbolen):
        # Controleren of de rooster grootte geldig is
        assert 2 <= n <= 10, 'er moet gelden dat 2 <= n <= 10'
        # Controleren of het aantal symbolen overeenkomt met de grootte van het rooster
        assert len(symbolen) == n * n, 'aantal symbolen komt niet overeen met grootte van het rooster'
        
        # Rooster in een lijst zetten, genummerd van 0 tot n-1 voor zowel rij als kolom
        self.n = n
        self.rooster = symbolen
        self.symbolen_dict = {symbolen[i]: (i // n, i % n) for i in range(len(symbolen))}
    
    def symbool(self, rij, kolom):
        """Retourneer het symbool op een gegeven rij en kolom"""
        # Controleer of de rij en kolom binnen de grenzen liggen
        if rij < 0 or rij >= self.n or kolom < 0 or kolom >= self.n:
            raise AssertionError("ongeldige positie in rooster")
        return self.rooster[rij * self.n + kolom]

    def positie(self, symbool):
        """Retourneer de rij en kolom van een gegeven symbool"""
        # Validatie van de invoer
        assert len(symbool) == 1, "symbool moet uit 1 karakter bestaan"
        if symbool not in self.symbolen_dict:
            raise AssertionError(f"onbekend symbool: '{symbool}'")
        return self.symbolen_dict[symbool]

    def codeer(self, tekst):
        """Codeer een tekst met de Bifid-codering"""
        rijen = []
        kolommen = []
        
        # Verkrijg de rijen en kolommen van de tekst
        for symbool in tekst:
            rij, kolom = self.positie(symbool)
            rijen.append(rij)
            kolommen.append(kolom)
        
        # Combineer de rijen en kolommen in één lange string
        rijen_str = ''.join(map(str, rijen))
        kolommen_str = ''.join(map(str, kolommen))
        
        # Maak nieuwe gecodeerde tekst door het combineren van de rijen en kolommen in paren
        gecodeerde_tekst = ""
        for i in range(0, len(rijen_str), 2):
            rij = int(rijen_str[i] + rijen_str[i+1])
            kolom = int(kolommen_str[i] + kolommen_str[i+1])
            gecodeerde_tekst += self.symbool(rij, kolom)
        
        return gecodeerde_tekst

    def decodeer(self, gecodeerde_tekst):
        """Decodeer een gecodeerde tekst terug naar de oorspronkelijke tekst"""
        rijen = []
        kolommen = []
        
        # Verkrijg de rijen en kolommen van de gecodeerde tekst
        for symbool in gecodeerde_tekst:
            rij, kolom = self.positie(symbool)
            rijen.append(rij)
            kolommen.append(kolom)
        
        # Split de rijen en kolommen weer op in twee delen
        rijen_str = ''.join(map(str, rijen))
        kolommen_str = ''.join(map(str, kolommen))
        
        # Maak de originele tekst door rijen en kolommen weer samen te voegen
        originele_tekst = ""
        for i in range(0, len(rijen_str), 2):
            rij = int(rijen_str[i] + rijen_str[i+1])
            kolom = int(kolommen_str[i] + kolommen_str[i+1])
            originele_tekst += self.symbool(rij, kolom)
        
        return originele_tekst
    
cijfer = Bifid(9, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdef' \
                    + 'ghijklmnopqrstuvwxyz .,;:?!"\'-()[]{}$=%')

# Testen van symbool en positie
print(cijfer.symbool(2, 1))  # 'T'
print(cijfer.positie('T'))   # (2, 1)

# Testen van coderen en decoderen
gecodeerde = cijfer.codeer('This is a dead parrot!')
print(gecodeerde)  # 'WgwygeexfozQ(%II5D$I}O'

origineel = cijfer.decodeer('WgwygeexfozQ(%II5D$I}O')
print(origineel)  # 'This is a dead parrot!'

