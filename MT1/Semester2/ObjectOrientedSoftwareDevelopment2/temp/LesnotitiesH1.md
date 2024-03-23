# OOSD II - Hoofdstuk 1 - Overerving

Verschillende datatypes:

| Primitief type | Referentie type |
| -------------- | --------------- |
| boolean | klassetype |
| byte, short, int, long, char | arraytype |
| float, double |  |

In het geval van een primitief datatype zit het datatype effectief op de plaats in het RAM. Terwijl bij referentie types zit daar enkel de verwijzing naar het adres in de Heap. In de heap bevindt zicht dan het datatype.

>[!caution]
>**Polymorfisme**: referentie variabele kan verwijzen naar verschillende type klassen. 

:arrow_right: Kan handig zijn om een lijst bij te houden van verschillende type variabelen of objecten.

## Klasse Object - methode equals

- Operator `==`: wordt gebruikt om waarden te vergelijken, in geval van referentiewaarden vergelijkt hij de adressen in het geheugen. (objecten met volledige dezelfde waarden en attributen maar een verschillend adres zullen `false` returnen)
- **Methode `equals(Object obj)`**: 
    - vergelijkt twee objecten en returned `true` als ze gelijk zijn anders `false`.
    - definieert de notie van gelijkheid op de toestand van een object, los van de referentie. (objecten met dezelfde waarden en attributen zullen `true` returnen)
    - `equals(Object obj)` methode komt altijd samen met de method `hashCode()` voor? 

>[!tip]
>Beide klassen kunnen gegenereerd worden door Eclipse :arrow_right:
>`right click > Source > "Generate hashCode() and equals()..."`

>[!important]
>Gebruik altijd `@Override` beide methodes worden geërft van de klasse `Object`

- **Methode `toString()`**: tekstvoorstelling van een object (meestal gedefineerd door de programmeur zelf)
- **Methode `getClass()`**: retourneert een referentie naar een instantie van de klasse `Class`. Geeft de runtime klasse van een object terug. (vb. een rechthoek-klasse kan ook een parent figuur-klasse hebben. Wanneer `getClass()` wordt aangeroepen zal dit altijd de rechthoek-klasse teruggeven)
Methode bevat verschillende info over de klasse, die via hulpmethodes kan aangeroepen worden
    - `getClass().getSimpleName()`: geeft `String` ipv `java.lang.String`
    - `getClass().getSuperClass()`: geeft de superklasse van de klasse


## Test-klassen Schrijven

>[!tip]
>Na het maken van een nieuwe package `testen` :arrow_right: `right click > new > JUnit Test case` bij het vervolledigen aanvinken om `JUnit library` te importeren

>[!tip]
>Tijdens het maken van de testklassen is het handig de klassen aan te vullen en `constructoren`, `getters` en `setters` te genereren

>[!tip]
>Bij het genereren van constructoren is kan je gemakkelijk `right click > source > generate getters and setters...`
> <br> Bij deze optie selecteer je getters en zet je ze `public` daarna opnieuwe dezelfde acties en selecteer je setters en zet je ze `private`

>[!important]
>Testen schrijf je altijd voor geldige waarden, ongeldige waarden en ook de randwaarden

>[!tip]
>Controleren of iets leeg is of geen spaties, tabs,... bevat doe je door het volgende:
>```java
>if(string == null || string.isBlank())
>```
>Belangrijk is om eerst te testen of de string `null` is want we kunnen `isBlank()` niet aanroepen open element dat `null` is

>[!tip]
>De `contains`-methode gebruikt de `equals`-methode om na te gaan of een object reeds bestaat in een lijst. Als we in een klasse zelf een `equals`-methode gespecifieer hebben zal hij ook deze gebruiken.


Wanneer krijgt een final attribuut zijn waarde?
- `static final` attribuut :arrow_right: bij declaratie van het attribuut
- `final` attribuut :arrow_right: krijgt waarde toegekend in constructor

>[!tip]
>Zoveel mogelijk `final` gebruiken

>[!important]
>Final objecten of arrays kunnen wel nog wijzigen. Het is enkel de referentie die final is

>[!caution]
>Private methode in de superklasse kan in de subklasse niet overschreven worden. De methode is private en dus niet toegankelijk

Indien een klasse final is zijn ook alle methodes binnen die klasse final

Abstracted-methodes zijn handig indien we op een referentie object (superklasse) de methode willen aanroepen. Vaak weten we op de moment van het aanroepen nog niet wat de implementatie van de methode zal zijn.