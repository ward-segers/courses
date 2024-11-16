# Web Develeopment 1 : Hoofdstuk 4 - CSS Basis - Deel 1

## CSS

> Cascading Style Sheets is een verzameling van stijlregels om webpagina's op te maken.

Door gebruik te maken van stijlregels is er een verschill tussen inhoud en opmaak

**Stijlregels** bestaan uit:
- een **selector** - duidt aan welk(e) HTML element beïnvloed worden
- een **declaration block** - een property:value paar
    - property: identifier die de in te stellen CSS-eigenschap definieert
    - value: waarde voor de in te stellen eigenschap

### CSS toevoegen aan een webpagina

Er zijn drie verschillende manieren om css aan een pagina toe te voegen:

- **external stylesheet**
    - wordt in een extern bestand geplaatst
    - via het `<link>`-element wordt het .css-bestand verbonden aan het HTML-document
    - meestal de verkozen manier
    ```html
    <head>
        ...
        <title>CSS</title>
        <link rel="stylesheet" href="style.css">
    </head>
    ```
- **internal stylesheet**
    - CSS rules bevinden zich in het HTML bestand zelf
    - binnen een `<style>`- element in de `<head>` van het HTML document
    ```html
    <head>
        ...
        <title>CSS</title>
        <style>
            h2{
                color:white;
                background-color:red;
            }
        </style>
    </head>
    ```
- **inline styles**
    - CSS declarations die slechts van toepassing zijn op één element
    - geplaatst in het style-attribuut voor dat element
    ```html
    <h2 style="color:white; background-color:red;">Header</h2>
    ```

### Backgrounds

- Elk element heeft een background, standaard is dit transparant
- instellen van een achtergrondkleur door `background-color`
- achtergrondafbeelding:
    - `background-image`: stelt de afbeelding in
    - `background-repeat`: stelt het herhalen van de afbeelding in todat alle ruimte in het block gevuld is
    - `background-attachement`: standaard schuift een afbeelding mee met de rest van de pagina, we kunnen deze met deze property vastzetten.
    - `background-position`: stelt de positionering in van de afbeelding
    - `background-clip`: stelt de overloop van de afbeelding in
    - `background-origin`: helpt bij de plaatsing van de afbeelding
    - `background-size`: stelt de schaal in van de afbeelding

    > Al deze properties kunnen ook samengevat worden in 1 property `background`

#### background-image

>[!TIP]
> Het is steeds verstandig om ook de achtergrondkleur in te stellen (tint van de afbeelding), dan weten we zeker dat het contrast met de andere inhoud blijft wanneer de afbeelding niet geladen kan worden.

- Het pad van de afbeelding is relatief tov de stylesheet en niet de webpagina
- Meerdere background-images zijn ook mogelijk

#### background-repeat

- Standaard wordt de afbeelding herhaald tot alle ruimte in het block gevuld is
- *repeat*: horizontaal en verticaal herhalen (standaard optie)
- *repeat-x*: horizontaal herhalen
- *repeat-y*: verticaal herhalen
- *no-repeat*: niet herhalen
- *space*: zo vaak als past en de resterende ruimte tussen de afbeeldingen gelijk verdelen
- *round* zo vaak als past en de resterende ruimte vullen door de afbeelding te schalen
- we kunnen ook 2 waarden opgeven: eerste voor de horizontale en tweede voor de verticale richting

    ```css
    background-repeat: repeat no-repeat;
    ```

#### background-attachement

Een afbeelding schuift standaard mee met de webpagina. We kunnen deze ook vastzetten:

- *fixed*: vast tov venster
- *scroll*: scrolt mee met element waarop het gedefinieerd is (standaard)
- *local*: meeschuiven met de inhoud van het element als dat een schuifbalk heeft

#### background-position

- Positie in het venster
- Je geeft een waarde op voor horizontale en verticale positie:
    - Sleutelwoorden: 
        - *left, center, right, top, bottom*
        - standaard: *left top*
    - Percentages:
        - standaard: *0% 0%*
    - Lengtes:
        - standaard: *0 0*

#### background shorthand property

Shorthand properties zijn de CSS properties waarmee je de waarde van verschillende CSS-properties in één keer kunt instellen. Zo is de `background`-property een shorthand property

Het stelt de `background-color`, `background-image`, `background-repeat`, `background-position` in één keer in

Bij de `background`-property moeten de waarden in de juiste volgorde staan, maar mogen er waarden ontbreken

<table>
<tr>
<th>Standaard</th>
<th>Shorthand property</th>
</tr>
<tr>
<td>

```css
background-color: #000;
background-image: url(images/bg.gif);
background-repeat: no-repeat;
background-position: left top;
```
</td>
<td>

```css
background: #000 url(images/bg.gif) no-repeat left top;
```
</td>
</tr>
</table>

Best gebruik je of de shorthand property of the longhand properties. Wanneer we beiden door elkaar gebruiken wordt door de shorthand property sommige waarden als standaard ingesteld. Dit kan enkel vermeden worden wanneer we een unieke manier van werken hanteren.

Onderstaand voorbeeld zal de achtergrondkleur niet op red instellen. Deze wordt overschreven door de standaard waarde transparent in de tweede regel

```css
background-color: red;
background: url(images/bg.gif) no-repeat left top;
```

### gradients

Gradients kunnen:
- lineair zijn:
    - `linear-gradient`
- radiaal zijn:
    - `radial-gradient`

### Kleuren

Voor elk element kan je
- de tekstkleur instellen met `color`
- de achtergrondkleur instellen met `background-color`

Daarnaast kan je ook nog de kleur instellen van randen, schaduwen,... met `border-color`, `text-shadow`

Instellen van kleuren kan je op volgende manieren:
- kleurnamen zoals red, blue,...
    ```css
    h1{color:red;}
    ```
- RGB: definieren van de red, green, blue waarden
    - absolute waarden: (waarden tussen 0 en 255)
        ```css
        h1{color:rgb(255 237 0);}
        ```
    - relatieve waarden: (percentage tussen 0% en 100%)
        ```css
        h1{color:rgb(100% 50% 0);}
        ```
    - hier kunnen we ook een 4<sup>de</sup> component definieren: alpha channel
        - deze komt overeen met het transparantie niveau
        - absolute waarden: (getal tussen 0 en 1)
            ```css
            h1{color:rgb(100% 50% 0 / 0.5);} /* helft transparant */
            ```
            ```css
            h1{color:rgb(100% 50% 0 / 1);} /* volledige dekking */
            ```
            ```css
            h1{color:rgb(100% 50% 0 / 0);} /* volledig transparant */
            ```
        - relatieve waarden: (percentage tussen 0% en 100%)
            ```css
            h1{color:rgb(100% 50% 0 / 50%);} /* helft transparant */
            ```
            ```css
            h1{color:rgb(100% 50% 0 / 100%);} /* volledige dekking */
            ```
            ```css
            h1{color:rgb(100% 50% 0 / 0%);} /* volledig transparant */
            ```

- hexadecimale notatie
    - begint met # en elke component krijgt een hexadecimale waarde tussen 00 en ff
        ```css
        h1{color:#ff7f00;}
        ```

### Lijsten opmaken

#### list-style-type

Wordt gebruikt om het opsommingsteken van een lijst te stijlen

```css
ol{
    list-style-type: upper-alpha; /* Zal hoofdletters instellen als opsommingsteken */
}

ul {
    list-style-type: none; /* Zal geen opsommingsteken instellen */
}
```

> Vaak worden unordered lists gebruikt om navigaties in te stellen. Meestal wordt de list-style-type op none ingesteld.

#### list-style-image

Wordt gebruikt om een afbeelding als opsommingsteken in te stellen

- We kunnen een eigen afbeelding instellen als een bullet
- Het pad is relatief tov het css-bestand niet tov de html-pagina

```css
ul{
    list-style-image: url(../images/star.png);
}
```

#### list-style-position

Wordt gebruikt om de positie van een opsommingsteken te stijlen

Kan ingesteld worden op *inside* of *outside (default waarde)*

```css
ul{
    list-style-image: url(../images/star.png);
    list-style-position: inside;
}
```

#### list-style

Wordt gebruikt als de shorthand om de lijst te stijlen

```css
ul{
    list-style: url(../images/star.png) inside;
}
```

### Tekst en typografie

