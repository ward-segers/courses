# Web Development 1 : Hoofdstuk 8 - Lay-out - Grid, float, postition

## CSS Grid

### Basisconcepten CSS Grid

> De CSS Grid Layout is een twee dimensionaal laypout model voor CSS. Het heeft veel mogelijkheden voor de **positionering** van boxes en hun inhoud, alsook voor het controleren van de afmetingen (sizing) van de boxes.

- Een grid betaat uit (denkbeeldige) horizontale en verticale lijnen die een grid container opdelen in rijen, kolommen en cellen. Te vergelijken met een tabel.

### Inleidend voorbeeld CSS Grid

Beschouw een element met daarin een aantal child elements.

<table>
<tr>
<th>Met Grid</th>
<th>Zonder Grid</th>
</tr>
<tr>
<td>

```html
<div class="grid-container">
    <div>item 1</div>
    <div>item 2</div>
    <div>item 3</div>
    <div>item 4</div>
    <div>item 5</div>
</div>
```
</td>
<td>

```html
<body>
    <header>Header</header>
    <nav>Navigation</nav>
    <main>Main area</main>
    <footer>Footer</footer>
</body>
```
</td>
</tr>
</table>

**Hoe gebruiken we hiervoor CSS Grid Layout?**

- Creëer een grind container met `display: block grid;` of (vroeger) `display: grid;`
    - het eerste deel `block` duidt aan dat de container een block element is
    - het tweede deel `grid` heeft als gevolg dat alle **directe** kind-elementen van deze `grid container`-element, grid items worden
    - we definiëren dus niet enkel de *grid container* maar ook impliciet de *grid items*

- Definieer *de grid* (het aantal rijen en/of kolommen en hun hoogte/breedte)
    - `grid-template-columns`
    - `grid-template-rows`

```css
.grid-container{
    display: block grid;
    grid-template-columns: 150px 150px 150px;
    grid-template-rows: 100px 100px 100px 100px;
}
```

> Note: grid items worden automatisch rij per rij in de grid geplaatst.

*Grid items positioneren op de grif met line numbers*:

```css
.grid-container{
    display: block grid;
    grid-template-columns: 150px 150px 150px;
    grid-template-rows: 100px 100px 100px 100px;
}
div:nth-of-type(2){
    grid-row: 3/5;
    grid-column: 2;
}
```

### CSS Grid Layout

Grid layout zorgt voor een goede scheiding tussen inhoud (html) en opmaak (css). We kunnen een html-element een andere positie op de grid geven zonder dat we daarvoor de markup (html) moeten wijzigen.

### Algemene procedure Grid Layout

1. Creëer een *grid container*. Hiermee definieer je impliciet ook de *grid items*
2. Definieer *de grid*
3. Plaats de *grid items* op de grid

#### Creëer de *grid container*


```css
display: block grid;
```