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

Dit kan door het creëren van een block-level-element:

```css
display: block grid;
```

> vroeger door: `display: grid;`

Dit kan ook door het creëren van een inline-level-element:

```css
display: inline grid;
```

> vroeger door: `display: inline-grid;`

Het maken van een *grid container* heeft als gevolg dat alle directe children *grid items* worden. Een `grid container` zelf is dus een block of een inline element.

#### Definieer de *grid*

Er zijn 3 properties die de expliciete grid van een grid container:

```css
grid-template-rows
grid-template-columns
grid-template-areas
```

De uiteindelijke grid kan uiteindelijk groter zijn door de grid-items die buiten de 'expliciete grid' geplaatst zijn.

In dat geval zullen er impliciet tracks gecreëerd worden.

De afmetingen van de tracks worden bepaald door `grid-auto-rows` en `grid-auto-columns`

##### `grid-template-rows` en `grid-template-columns`

De waarde van `grid-template-rows` (en `grid-template-columns`) kan een **\<track-list>** of een \<auto-track-list>

Mogelijke track-sizes bij een \<track-list> zijn:

- \<length>
- \<percentage>
- \<flex>
- min-content
- max-content
- minmax(min, max)
- fit-content(value)
- auto

voorbeelden \<track-list>:

```css
grid-template-columns: 20ch 200px 200px;
grid-template-columns: 20% 40% 60%;
grid-template-columns: 100px 1fr 2fr;
grid-template-columns: minmax(100px, 200px);
grid-template-columns: fit-content(40%);
grid-template-columns: auto 100px 1fr;
```

*de fr-eenheid (\<flex> CSS data type)*

- Met de fr-eenheid kan je 'flexible grid tracks' (rijen of kolommen) maken.
- De fr-eenheid stelt een fractie in van de 'leftover space'. De leftover space komt overeen met de ruimte die niet ingenomen wordt door de 'non-flexible grid tracks'

*`repeat()`-functie*

Met de `repeat()`-functie kan je een deel van de 'track-list' herhalen

<table>
<tr>
<th>

Old
</th>
<th>

with `repeat()`-functie
</th>
</tr>
<tr>
<td>

```css
grid-template-rows: 1fr 1fr 1fr;
```
</td>
<td>

```css
grid-template-columns: repeat(3, 1fr);
```
</td>
</tr>
<tr>
<td>

```css
grid-template-columns: 20px 1fr 2fr 1fr 2fr 1fr 2fr 1fr 2fr;
```
</td>
<td>

```css
grid-template-columns: 20px repeat(4, 1fr 2fr);
```
</td>
</tr>
</table>

##### `grid-auto-rows` en `grid-auto-columns`

- in de vorige voorbeelden hebben we de kolommen (column tracks) expliciet gedefinieerd met `grid-template-columns`-property en hebben we de rijen impliciet gecreëerd.
- het instellen van de hoogte van deze impliciet gecreëerde rijen doe je via `grid-auto-rows` (analoog voor de kolommen)
- de initial value voor deze properties is **auto**. Impliciet gecreëerde rijen (en kolommen) zijn dus 'auto-sized'.
- ook hier kunnen we dezelfde 'track-sizes' gebruiken (bv. `minmax()`)

*`repeat()` met `auto-fill` en `auto-fit`*

- De waarde voor grid-template-columns (en grid-template-rows) kan
niet alleen een \<track-list> zijn (zie vroeger), maar ook een \<auto-track-
list>.
- Bij een \<auto-track-list> gaan we bij de `repeat()`-functie, als eerste
argument i.p.v. een getal op te geven, de waarde auto-fill of auto-
fit gebruiken.

voorbeeld:
```css
grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
```

Bij dit voorbeeld geven we zelf geen vast aantal kolommen op bij de `repeat()`-functie maar laten we de browser het aantal kolommen bepalen `auto-fill`

De overige leegruimte wordt automatisch verdeeld tussen het aantal tracks.

> `auto-fill` en `auto-fit` werken op dezelfde manier, behalve als er lege tracks zijn.

#### positioneren van grid items op de grid

> Grid items kunnen ook over meerdere rijen en kolommen overspannen.

- Als je *grid lines* definieert dan krijgen de lijnen waaruit de grid bestaat automatische nummers. Je kan dan deze lijnnummers gebruiken om een *grid item* expliciet te positioneren op de grid.

>[!tip]
> Gebruik inspector, layout, om de line numbers, line names van de grid te tonen.

- De getallen verwijzen naar de lijnen en niet naar de kolommen
- Er zijn ook negatieve lijnnummers mogelijk.

voorbeeld:

<table>
<tr>
<td>

```css
.box1 {grid-column-start: 1; grid-column-end: 2; grid-row-start: 1; grid-row-end: 4;}
.box2 {grid-column-start: 3; grid-column-end: 4; grid-row-start: 1; grid-row-end: 3;}
.box3 {grid-column-start: 2; grid-column-end: 3; grid-row-start: 1; grid-row-end: 2;}
.box4 {grid-column-start: 2; grid-column-end: 4; grid-row-start: 3; grid-row-end: 4;}
```
</td>
<td>

```html
<div class="grid-container">
    <div class="box1">One</div>
    <div class="box2">Two</div>
    <div class="box3">Three</div>
    <div class="box4">Four</div>
</div>
```
</td>
</tr>
<tr>
<td colspan="2">

<p align='center'><img src='src/css_grid_positioneren.png' alt='Positioneren in de grid' width='50%'></p>

</td>
</tr>
</table>