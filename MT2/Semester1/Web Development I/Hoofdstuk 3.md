# Web Develeopment 1 : Hoofdstuk 3 - Tabellen en Formulieren

## Tabellen

Een tabel is een rechthoekig raster van rijen en kolommen. Waar kolommen en rijen kruisen krijgt men cellen. Elke cel kan informatie bevatten: tekst, getallen, koppelingen, afbeeldingen,...

**Syntax**:

Elke tabel begint met de `<table>`-tag.
Een rij wordt opgebouwd door de `<tr>`-tag.
Een cell kan bestaan uit een heading (`<th>`) of een datacel (`<td>`)

<table>
<tr>
<th>Syntax</th>
<th>Output</th>
</tr>
<tr>
<td

```html
<table>
<tr>
<th>Eerste heading</th>
<th>Tweede heading</th>
</tr>
<tr>
<td>Eerste datacel</td>
<td>Tweede datacel</td>
</tr>
</table>
```

</td>
<td>

<table>
<tr>
<th>Eerste heading</th>
<th>Tweede heading</th>
</tr>
<tr>
<td>Eerste datacel</td>
<td>Tweede datacel</td>
</tr>
</table>

</td>
</tr>
</table>

**Kenmerken**:
- Binnen elke cel loopt tekst automatisch door naar de volgende regel als de tekst te lang wordt binnen de cel.
- De meeste tags zoals `<strong>`, `<em>`, `<hr>`, `<img>`,... kan je gebruiken binnen een cel
- Standaardopmaak:
    - `<th>` - hoofding voor rij en kolom: inhoud standaard gecentreerd en vet
    - `<td>` - gewone cellen: inhoud staat links gealigneerd
- Binnen elke cel kan je een nieuwe tabel beginnen (=geneste tabellen)

### Opmaak

Ook bij tabellen kunnen we de opmaak wijzigen door middel van css.

- Rand rond tabel en cellen:

    ```css
    table, th, td{
        border: 1px solid black;
    }
    ```

- Dit zorgt voor een probleem namelijk een dubbele rand. Oplossing is collapsing border gebruiken:

    ```css
    table{
        border-collapse: collapse;
    }
    ```
- Voorbeeld met enkel onderrand en witruimte:

    ```css
    table{
        border-collapse:collapse;
        font-size: 14px;
    }
    table, th, td{
        border-block-end: 1px solid black; /* bottom line  */
        padding: 10px 15px; /* 10px boven witruimte, 15px links en rechts  */
    }
    ```

We kunnen via HTML verschillende kolommen groeperen en op deze manier de kolommen samen eenzelfde opmaak geven.

Hiervoor gebruiken we de `<colgroup>`-tag.

- We specifiëren steeds de breedte waarover de groep zich spreid (via een span attribuut)
- We kunnen verschillende klasses toewijzen aan de groep doormiddel van een class attribuut
- We kunnen enkel border, background, visibilty en width properties toekennen via een "colgroup"
- voorbeeld: (groupeert de eerste 3 kolommen en wijst aan de volgende kolom de klasse last toe)
    ```html
    <colgroup>
        <col span="3">
        <col class="last">
    </colgroup>
    ```

### Structuur

Cellen kunnen ook samenengevoegd worden. We kunnen dit zowel over de kollommen als over de rijen.

- Samenvoegen cellen over 3 kolommen

    ```html
    <tr>
        <td colspan="3">Celinhoud</td>
        <td>Celinhoud</td>
    </tr>
    ```
- Samenvoegen cellen over 2 rijen

  ```html
    <tr>
        <td rowspan="2">Celinhoud</td>
        <td>Celinhoud</td>
    </tr>
    ```

Vaak kunnen we tabellen onderscheiden in de volgende items:

- header
- body
- footer

In HTML kunnen we deze beschrijven met volgende tags:

- `<thead>`
- `<tbody>`
- `<tfoot>`

> Deze informatie is interessant voor de screen readers en voor de opmaak in CSS.

In HTML tabellen kunnen we bijschriften schrijven doormiddel van de `<caption>`-tag. 

Deze wordt standaard boven de tabel weergegeven. Echter kunnen we dit doormiddel van CSS wel wijzigen:

```css
caption{
    caption-side: block-end;
}
```

## Formulieren

Doormiddel van formulieren (forms) kan men gegevens van de gebruiker verzamelen. We kunnen deze gebruiken oim:

- je aan te melden op een website
- een online bestelling te maken
- te zoeken
- te chatten
- te bloggen
- te twitteren
- ...

Binnen deze formulieren zijn er verschillende mogelijkheden