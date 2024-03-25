# OOSD II - Hoofdstuk 2 - Polymorfisme en interfaces

## Polymorfisme

Binnen Java betekent polymorfisme dat een referentie variabele van een bepaald type kan verwijzen naar objecten van verschillende types: het type zelf of één van zijn subtypes.

>[!tip]
>Dankzij polymorfisme kan je achteraf nog subklasse toevoegen die de eigenschappen en het gedrag van de subklasse overnemen. 

**Polymorfisme of veelvormigheid** komt voort uit een "IS EEN" relatie: overerving. 

<p align='center'><img src='src/voorbeeld_klasse_hierarchie.png' alt='Voorbeeld klasse hiërarchie' width='50%'></p>

Een superklasse referentie kan refereren naar een instantie van een subklasse. Dit noemt men _upcasting_