# Web Development 1 : HTML basis deel 1 - CCS intro

## Inleiding

Wanneer we surfen naar een webadres op het internet:

https://www.google.com

Doen we eigenlijke een verzoek aan een server om een webpagina naar jouw toestel terug te sturen. Indien deze pagina op de server staat zal ze door de server terug gegeven worden, hierna bouwt de browser (de client) deze webpagina op en geeft ze weer.

Een browser (de client) begrijpt 3 verschillende talen:

- **HTML**: "Hypertext Markup Language" de taal die gebruikt wordt om de pagina's te beschrijven. Je brengt met behulp van HTML **structuur** en **betekenis** (semantiek) aan de webpagina. In heel eenvoudige vorm staat HTML ook toe interacties aan te maken met de gebruiker. (knoppen om op te klikken,...)
- **CSS**: "Cascading Stylesheet" de taal waarmee je de **layout** en de **opmaak** van de pagina beschrijft. Ook hier zijn eenvoudige interacties met de gebruiker mogelijk. (bv. acties wanneer we hoveren over een afbeelding,...)
- **Javascript**: de taal waarmee je **complexe interacties** aan de webpagina kan toevoegen.

## HTML

De drie belangrijkste element:

- *element*: een element wordt aangeduidt met een openings- en sluitingstag. 
    - Sommige elementen hebben enkel een openingstag. Deze noemen we *void elementen*
    - Voorbeeld: `<br>`
- *tag*: een onderdeel van een element (opening of sluiting van het element)
- *attribute*: bevatten meer informatie over een element.
    - Elementen kunnen geen, één of meerdere attributen hebben
    - Bevat een naam, waarde
    - Staat in de openingstag net na de tag-naam
    - Syntax: `attribute name="attribute value"`

## CSS

De belangrijkste begrippen zijn:

- *selector*: duidt aan welke html-elementen beïnvloed worden door de stijlregel.
- *style rule*
- *declaration*
- *property*: de css-eigenschap die je wil instellen
- *value*: de waarde voor deze eigenschap

### CSS Selectors

Er bestaan verschillende type css selectors:

- *Type selector*:
    - Selecteren alle elementen van een bepaald type
    - Indien we alle div-elementen willen selecteren:
    ```css
        div{...}
    ```
- *Class selector*: 
    - Laten toe om verschillende elementen te selecteren en dezelfde opmaak te geven.
    - We geven deze elementen dan dezelfde class-value
    - Indien we alle elementen met de klasse awesome willen selecteren:
    ```css
        .awesome{...}
    ```
- *ID selector*:
    - Worden gebruikt om een uniek element op de webpagina te selecteren.
    - We geven aan elk element een unieke ID die slechts eenmaal op de webpagina mag voorkomen.
    - ID's worden minder gebeurd dan classes
    - Indien we een element met ID shayhowe willen selecteren:
    ```css
        #shayhowe{...}
    ```
- *Group selector*:
    - Worden gebruikt wanneer je dezelfde stijl wil geven aan verschillende css selectoren
    - De css selectoren worden gescheiden door een komma.
    ```css
        h1, .awesome, p{...}
    ```

