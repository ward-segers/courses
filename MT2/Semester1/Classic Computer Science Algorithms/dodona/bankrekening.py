# https://dodona.be/nl/courses/4195/series/46776/activities/2096226599


class BankRekening:
    def __init__(self, naam, rekeningnummer, bedrag=0):
        """
        Initialiseer een nieuwe bankrekening.
        
        Parameters:
            naam (str): Naam van de rekeninghouder.
            rekeningnummer (str): Het rekeningnummer.
            bedrag (float): Het startbedrag op de rekening. Standaard 0.
        """
        self.naam = naam
        self.rekeningnummer = rekeningnummer
        self.bedrag = bedrag

    def storten(self, n):
        """
        Stort een bedrag bij op de rekening.
        
        Parameters:
            n (float): Het bedrag om te storten.
        """
        self.bedrag += n

    def afhalen(self, n):
        """
        Haalt een bedrag van de rekening af.
        
        Parameters:
            n (float): Het bedrag om af te halen.
        """
        self.bedrag -= n

    def __str__(self):
        """
        Geeft een stringrepresentatie van de bankrekening die leesbaar is voor de gebruiker.
        
        Returns:
            str: De stringrepresentatie van de bankrekening.
        """
        return f"{self.naam}, {self.rekeningnummer}, bedrag: {self.bedrag}"

    def __repr__(self):
        """
        Geeft een formele representatie van de bankrekening die kan worden geëvalueerd door de Python interpreter.
        
        Returns:
            str: Een expressie die het object representeert.
        """
        return f"BankRekening('{self.naam}', '{self.rekeningnummer}', {self.bedrag})"

# Voorbeeld van gebruik
b1 = BankRekening('Jan Jansen', '001457894501', 10000)
b2 = BankRekening('Peter Peeters', '842457894511', 10000)
b1.storten(250)
b1.afhalen(1000)
b2.afhalen(300)

print(str(b1))  # Output: Jan Jansen, 001457894501, bedrag: 9250
print(b2)       # Output: Peter Peeters, 842457894511, bedrag: 9700
print(repr(b2)) # Output: BankRekening('Peter Peeters', '842457894511', 9700)

b3 = BankRekening('David Davidse', '002457896312')
b3.storten(112)
print(b3)       # Output: David Davidse, 002457896312, bedrag: 112
print(repr(b3)) # Output: BankRekening('David Davidse', '002457896312', 112)
