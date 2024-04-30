# OOSD II - Hoofdstuk 4 - Exception handling

Exception gebeurd niet altijd, soms. Als er een "uitzondering" is stoppen we het normaal verloop van het programma

Stack trace => deel van de exceptie die weergeeft waar de fout zicht voordoet.

>[!tip]
>Rood printen in de console: `System.err` ipv `System.Out`

Let op waar je try-catch blok plaats.
Welke zaken mogen wel of niet uitgevoerd worden bij een exception

>[!tip]
>In **Javadoc** kan je extra info meegeven:

```java
/** Algemene beschrijving van wat bv een methode doet
 * @return beschrijft wat de methode returns
 * @throws beschrijft welke exceptie de methode kan gooien
 * /
```

>[!tip]
>Bekijk in je methodes welke exceptions kunnen gegooid worden


Stukken die verder bouwen op het stuk waar een exceptie op gegooid wordt moeten binne het try-blok staan

Finally wordt altijd uitgevoerd (ook bij exceptie) => Handig om resources af te sluiten

**Best practise**: wees zo specifiek mogelijk met de excepties die je opvangt.

>[!caution]
>Wanneer je een InputMismatchException opvangt moet je steeds de buffer legen door in de catch:

```java
scannerObject.nextLine();
```

**Best practise**: aanvaard strings van de gebruiker als invoer en probeer ze achteraf om te zetten naar int, of double

2 soorten exceptions:
- checked - moet afgehandeld worden
- unchecked (kan ook error) - geen probleem voor compiler als deze niet afgehandeld worden.

>[!tip]
>Aanmaken van Exception-klassen kan gemakkelijk een bijna automatische vanuit eclipse:
>src > new class > Package = exceptions > geef de superklasse in (van welke exception erft deze exception?) > Selecteer "Constructors from superklasse"

Belangrijk is om te weten waar de exceptie opgevangen zal worden. (vaak niet in de setters => geen feedback naar de user)